# tests/test_foundation_config.py
# Unit tests for foundation/config.py

"""Unit tests for the foundation.config module."""

import io
import json
import os
import sys
import tempfile
import unittest
from unittest.mock import patch
from argparse import Namespace
from pathlib import Path

from core.presets import NO_PRESET, PRESET_CHOICES
from core.config import (
    CONFIG_KEY_MAPPING,
    DEFAULT_VALUES,
    ConfigFileError,
    _read_config_file,
    apply_preset_to_args,
    build_parser,
    find_config_file,
    include_option_help,
    load_config,
    load_config_file,
    merge_config_with_args,
    normalize_config_preset,
    validate_arguments,
)


class TestConfigKeyMapping(unittest.TestCase):
    """Test configuration key mapping."""

    def test_mapping_has_required_keys(self):
        """Mapping should include all core config options."""
        required_keys = ["project_name", "author_name", "license", "output_dir"]
        for key in required_keys:
            self.assertIn(key, CONFIG_KEY_MAPPING)

    def test_mapping_supports_multiple_naming_conventions(self):
        """Mapping should support snake_case, kebab-case, and camelCase."""
        # Check project_name variations
        self.assertEqual(CONFIG_KEY_MAPPING["project_name"], "project_name")
        self.assertEqual(CONFIG_KEY_MAPPING["project-name"], "project_name")
        self.assertEqual(CONFIG_KEY_MAPPING["projectName"], "project_name")


class TestDefaultValues(unittest.TestCase):
    """Test default values."""

    def test_required_fields_are_none(self):
        """Required fields should default to None."""
        self.assertIsNone(DEFAULT_VALUES["project_name"])
        self.assertIsNone(DEFAULT_VALUES["author_name"])

    def test_license_defaults_to_mit(self):
        """License should default to MIT."""
        self.assertEqual(DEFAULT_VALUES["license"], "mit")

    def test_boolean_options_default_to_false(self):
        """Boolean options should default to False."""
        boolean_keys = [
            "include_coc",
            "include_security",
            "include_github_templates",
            "include_changelog",
            "include_all",
            "include_enhanced_security",
            "include_secrets_detection",
            "include_adr",
            "include_ci",
            "verbose",
            "non_interactive",
            "accept_terms",
        ]
        for key in boolean_keys:
            self.assertFalse(DEFAULT_VALUES[key], f"{key} should default to False")


class TestLoadConfigFile(unittest.TestCase):
    """Test configuration file loading."""

    def test_returns_empty_dict_when_no_config(self):
        """Should return empty dict when no config file exists."""
        with tempfile.TemporaryDirectory() as tmpdir:
            original_cwd = os.getcwd()
            try:
                os.chdir(tmpdir)
                config = load_config_file()
                self.assertEqual(config, {})
            finally:
                os.chdir(original_cwd)

    def test_loads_explicit_config_path(self):
        """Should load config from explicit path."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "test_config.json"
            config_path.write_text(json.dumps({"project_name": "TestProject"}))
            config = load_config_file(str(config_path))
            self.assertEqual(config.get("project_name"), "TestProject")

    def test_empty_object_in_explicit_config_is_not_an_error(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "empty.json"
            config_path.write_text("{}")
            with patch("sys.stdout", new_callable=io.StringIO):
                self.assertEqual(load_config_file(str(config_path)), {})

    def test_missing_explicit_config_is_an_error(self):
        """A --config file that doesn't exist used to warn and continue (#150)."""
        with tempfile.TemporaryDirectory() as tmpdir:
            missing = str(Path(tmpdir) / "missing.json")
            with self.assertRaises(ConfigFileError) as raised:
                load_config_file(missing)
        message = str(raised.exception)
        self.assertIn(f"Config file not found: '{missing}'.", message)

    def test_invalid_json_in_explicit_config_is_an_error(self):
        """Invalid JSON used to print an error and continue (#150)."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "invalid_config.json"
            config_path.write_text("not valid json {{{")
            with self.assertRaises(ConfigFileError) as raised:
                load_config_file(str(config_path))
        self.assertIn(f"The config file '{config_path}' is not valid JSON: ",
                      str(raised.exception))

    def test_explicit_config_that_is_not_a_json_object_is_an_error(self):
        for text, kind in [('["preset"]', "array"), ('"standard"', "string"), ("3", "number"),
                           ("true", "boolean"), ("null", "null")]:
            with self.subTest(text=text), tempfile.TemporaryDirectory() as tmpdir:
                config_path = Path(tmpdir) / "config.json"
                config_path.write_text(text)
                with self.assertRaises(ConfigFileError) as raised:
                    load_config_file(str(config_path))
                message = str(raised.exception)
                self.assertIn(f"The config file '{config_path}' must hold a JSON object",
                              message)
                self.assertIn(f"it holds a JSON {kind}", message)

    def test_explicit_config_that_is_a_directory_is_an_error(self):
        """Opening a directory gives "[Errno 13] Permission denied" on Windows."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with self.assertRaises(ConfigFileError) as raised:
                load_config_file(tmpdir)
        message = str(raised.exception)
        self.assertEqual(message,
                         f"The config file '{tmpdir}' is not a file; it is a directory.")
        self.assertNotIn("Errno", message)

    def test_config_that_cannot_be_opened_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"
            config_path.write_text("{}")
            with patch("builtins.open", side_effect=PermissionError(13, "Permission denied")):
                with self.assertRaises(ConfigFileError) as raised:
                    load_config_file(str(config_path))
        self.assertIn(f"Cannot read the config file '{config_path}': ", str(raised.exception))

    def test_explicit_config_that_is_not_utf8_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"
            config_path.write_bytes(b'{"project_name": "caf\xe9"}')
            with self.assertRaises(ConfigFileError) as raised:
                load_config_file(str(config_path))
        self.assertIn(f"Cannot read the config file '{config_path}': ", str(raised.exception))

    def test_deeply_nested_json_is_an_error(self):
        """The parser raises RecursionError, which used to end the run with a traceback."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "deep.json"
            config_path.write_text("[" * 100000 + "]" * 100000)
            with self.assertRaises(ConfigFileError) as raised:
                load_config_file(str(config_path))
        self.assertEqual(str(raised.exception),
                         f"Cannot read the config file '{config_path}': its arrays or "
                         "objects are nested too deeply.")

    @unittest.skipUnless(getattr(sys, "get_int_max_str_digits", lambda: 0)(),
                         "this Python has no limit on the digits in an integer")
    def test_integer_with_too_many_digits_is_an_error_that_names_the_file(self):
        """The parser raises a plain ValueError whose message does not name the file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "big.json"
            config_path.write_text('{"preset": ' + "9" * (sys.get_int_max_str_digits() + 1) + "}")
            with self.assertRaises(ConfigFileError) as raised:
                load_config_file(str(config_path))
        message = str(raised.exception)
        self.assertEqual(f"The config file '{config_path}' holds a number too long to read.", message)

    def test_other_parser_value_error_is_reported_with_its_own_text(self):
        """Only the digit-limit error is described as a number too long to read."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"
            config_path.write_text("{}")
            with patch("core.config.json.loads", side_effect=ValueError("unexpected value")):
                with self.assertRaises(ConfigFileError) as raised:
                    load_config_file(str(config_path))
        self.assertEqual(str(raised.exception),
                         f"Cannot read the config file '{config_path}': unexpected value.")

    def test_path_check_that_fails_while_reading_is_an_error_that_names_the_file(self):
        """A parent directory that denies access makes `Path.is_dir()` raise on POSIX."""
        denied = PermissionError(13, "Permission denied")
        for method in ("is_symlink", "exists", "is_dir", "is_file"):
            with self.subTest(method=method), tempfile.TemporaryDirectory() as tmpdir:
                config_path = Path(tmpdir) / "config.json"
                config_path.write_text("{}")
                if method == "is_file":
                    # is_file() is asked only about a path that exists and is no directory.
                    config_path = Path(os.devnull)
                with patch.object(Path, method, side_effect=denied):
                    with self.assertRaises(ConfigFileError) as raised:
                        _read_config_file(config_path)
                self.assertEqual(
                    str(raised.exception),
                    f"Cannot read the config file '{config_path}': {denied}.")

    def test_path_check_that_fails_while_finding_is_an_error_that_names_the_file(self):
        """The same failure in find_config_file(), for --config and for the default names."""
        denied = PermissionError(13, "Permission denied")
        explicit = str(Path("no-access") / "config.json")
        for method in ("exists", "is_symlink"):
            with self.subTest(method=method), patch.object(Path, method, side_effect=denied):
                with self.assertRaises(ConfigFileError) as raised:
                    find_config_file(explicit)
                self.assertEqual(str(raised.exception),
                                 f"Cannot read the config file '{explicit}': {denied}.")
                with self.assertRaises(ConfigFileError) as raised:
                    self._load_from({})
                self.assertEqual(str(raised.exception),
                                 f"Cannot read the config file '.foundationrc': {denied}.")

    def test_utf8_byte_order_mark_is_accepted(self):
        """Some Windows editors start a UTF-8 file with a byte-order mark."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "bom.json"
            config_path.write_bytes(b'\xef\xbb\xbf{"project_name": "caf\xc3\xa9"}')
            self.assertEqual(load_config_file(str(config_path)), {"project_name": "caf\u00e9"})

    def test_empty_config_is_an_error_that_says_so(self):
        """An empty file used to report "Expecting value: line 1 column 1 (char 0)"."""
        for content in [b"", b" \n\t\r\n", b"\xef\xbb\xbf", b"\xef\xbb\xbf\n"]:
            with self.subTest(content=content), tempfile.TemporaryDirectory() as tmpdir:
                config_path = Path(tmpdir) / "empty.json"
                config_path.write_bytes(content)
                with self.assertRaises(ConfigFileError) as raised:
                    load_config_file(str(config_path))
                self.assertEqual(str(raised.exception),
                                 f"The config file '{config_path}' is empty. "
                                 "Write {} in it, or delete it.")

    def test_loading_prints_nothing(self):
        """The caller prints "Loaded config" after it has checked the settings."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"
            config_path.write_text('{"preset": "standrad"}')
            with patch("sys.stdout", new_callable=io.StringIO) as stdout:
                config, config_file = load_config(str(config_path))
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(config, {"preset": "standrad"})
        self.assertEqual(config_file, config_path)

    def test_load_config_names_no_file_when_there_is_none(self):
        self.assertEqual(self._load_from({}, loader=load_config), ({}, None))

    def _load_from(self, files, loader=load_config_file):
        """Call load_config_file() in a directory that holds the given files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            for name, text in files.items():
                if text is None:
                    (Path(tmpdir) / name).mkdir()
                else:
                    (Path(tmpdir) / name).write_text(text)
            original_cwd = os.getcwd()
            try:
                os.chdir(tmpdir)
                with patch("sys.stdout", new_callable=io.StringIO):
                    return loader()
            finally:
                os.chdir(original_cwd)

    def test_loads_auto_found_config(self):
        from core.utils import CONFIG_FILES
        for name in CONFIG_FILES:
            with self.subTest(name=name):
                self.assertEqual(self._load_from({name: '{"preset": "light"}'}),
                                 {"preset": "light"})

    def test_auto_found_config_with_invalid_json_is_an_error(self):
        """An auto-found file with invalid JSON used to be skipped silently (#150)."""
        from core.utils import CONFIG_FILES
        for name in CONFIG_FILES:
            with self.subTest(name=name):
                with self.assertRaises(ConfigFileError) as raised:
                    self._load_from({name: "{ not json"})
                self.assertIn(f"The config file '{name}' is not valid JSON: ",
                              str(raised.exception))

    def test_auto_found_config_that_is_not_a_json_object_is_an_error(self):
        with self.assertRaises(ConfigFileError) as raised:
            self._load_from({".foundationrc": "[1, 2]"})
        message = str(raised.exception)
        self.assertIn("The config file '.foundationrc' must hold a JSON object", message)
        self.assertIn("it holds a JSON array", message)

    def test_auto_found_config_that_is_a_directory_is_an_error(self):
        with self.assertRaises(ConfigFileError) as raised:
            self._load_from({".foundationrc": None})
        self.assertEqual(str(raised.exception),
                         "The config file '.foundationrc' is not a file; it is a directory.")

    def test_auto_found_empty_config_is_an_error(self):
        with self.assertRaises(ConfigFileError) as raised:
            self._load_from({".foundationrc": "", "foundationrc.json": '{"preset": "light"}'})
        self.assertIn("The config file '.foundationrc' is empty.", str(raised.exception))

    def test_symlink_with_a_missing_target_is_an_error(self):
        """`Path.exists()` is False for such a link, so it used to be skipped silently."""
        from core.utils import CONFIG_FILES
        for name in CONFIG_FILES:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmpdir:
                try:
                    os.symlink(Path(tmpdir) / "missing-target", Path(tmpdir) / name)
                except (OSError, NotImplementedError) as error:
                    self.skipTest(f"cannot create symbolic links here: {error}")
                original_cwd = os.getcwd()
                try:
                    os.chdir(tmpdir)
                    with self.assertRaises(ConfigFileError) as raised:
                        load_config_file()
                    explicit = str(Path(tmpdir) / name)
                    with self.assertRaises(ConfigFileError) as raised_explicit:
                        load_config_file(explicit)
                finally:
                    os.chdir(original_cwd)
                self.assertEqual(str(raised.exception),
                                 f"Cannot read the config file '{name}': it is a symbolic "
                                 "link, and its target does not exist.")
                self.assertIn(f"Cannot read the config file '{explicit}': it is a symbolic link",
                              str(raised_explicit.exception))

    def test_symlink_with_a_missing_target_is_an_error_without_real_symlinks(self):
        """The same rule, checked where the OS or permissions can't create symlinks."""
        def is_dangling_link(path):
            return path.name == ".foundationrc"

        with patch.object(Path, "is_symlink", is_dangling_link):
            with self.assertRaises(ConfigFileError) as raised:
                self._load_from({"foundationrc.json": '{"preset": "light"}'})
            self.assertEqual(str(raised.exception),
                             "Cannot read the config file '.foundationrc': it is a symbolic "
                             "link, and its target does not exist.")
            with tempfile.TemporaryDirectory() as tmpdir:
                explicit = str(Path(tmpdir) / ".foundationrc")
                with self.assertRaises(ConfigFileError) as raised:
                    load_config_file(explicit)
            self.assertIn(f"Cannot read the config file '{explicit}': it is a symbolic link",
                          str(raised.exception))

    def test_broken_auto_found_config_does_not_fall_back_to_the_next_name(self):
        """The valid foundationrc.json must not hide the broken .foundationrc."""
        with self.assertRaises(ConfigFileError) as raised:
            self._load_from({".foundationrc": "{ not json",
                             "foundationrc.json": '{"preset": "light"}'})
        self.assertIn("The config file '.foundationrc' is not valid JSON",
                      str(raised.exception))


class TestMergeConfigWithArgs(unittest.TestCase):
    """Test merging config with command-line arguments."""

    def test_config_applies_to_default_values(self):
        """Config values should apply when args have default values."""
        args = Namespace(
            project_name=None,
            author_name=None,
            license="mit",
        )
        config = {"project_name": "FromConfig", "author_name": "Config Author"}
        result = merge_config_with_args(args, config)
        self.assertEqual(result.project_name, "FromConfig")
        self.assertEqual(result.author_name, "Config Author")

    def test_cli_args_override_config(self):
        """CLI arguments should override config values."""
        args = Namespace(
            project_name="FromCLI",
            author_name=None,
            license="mit",
        )
        config = {"project_name": "FromConfig", "author_name": "Config Author"}
        result = merge_config_with_args(args, config)
        self.assertEqual(result.project_name, "FromCLI")
        self.assertEqual(result.author_name, "Config Author")


class TestApplyPresetToArgs(unittest.TestCase):
    """A preset turns its features on and never turns a requested feature off."""

    def test_preset_turns_its_features_on(self):
        args = Namespace(include_ci=False, include_adr=False)
        preset = {"features": {"ci_workflow": True, "adr": False}}
        result = apply_preset_to_args(args, preset)
        self.assertTrue(result.include_ci)
        self.assertFalse(result.include_adr)

    def test_preset_does_not_turn_requested_features_off(self):
        args = Namespace(include_ci=False, include_adr=True)
        preset = {"features": {"ci_workflow": True, "adr": False}}
        result = apply_preset_to_args(args, preset)
        self.assertTrue(result.include_adr)

    def test_empty_preset_changes_nothing(self):
        args = Namespace(include_adr=True)
        self.assertTrue(apply_preset_to_args(args, {}).include_adr)


class TestNoPresetChoice(unittest.TestCase):
    """`--preset none` parses, applies nothing, and is accepted in a config file (#137)."""

    def test_preset_none_parses(self):
        args = build_parser().parse_args(["--preset", "none"])
        self.assertEqual(args.preset, NO_PRESET)

    def test_command_line_preset_accepts_any_case(self):
        """--list-presets prints the heading NONE, so `--preset NONE` has to work."""
        for given, expected in [("NONE", NO_PRESET), ("None", NO_PRESET),
                                ("Standard", "standard"), ("ENTERPRISE", "enterprise")]:
            with self.subTest(given=given):
                args = build_parser().parse_args(["--preset", given])
                self.assertEqual(args.preset, expected)

    def test_command_line_preset_still_rejects_unknown_values(self):
        with patch("sys.stderr", new_callable=io.StringIO), self.assertRaises(SystemExit):
            build_parser().parse_args(["--preset", "everything"])

    def test_preset_none_on_command_line_overrides_config_preset(self):
        """Leaving --preset out takes the config file's preset; `--preset none` cancels it."""
        config = {"preset": "standard"}
        omitted = merge_config_with_args(build_parser().parse_args([]), dict(config))
        self.assertEqual(omitted.preset, "standard")
        none = merge_config_with_args(
            build_parser().parse_args(["--preset", "none"]), dict(config))
        self.assertEqual(none.preset, NO_PRESET)

    def test_config_preset_accepts_any_case(self):
        for given, expected in [("NONE", NO_PRESET), ("None", NO_PRESET),
                                ("Standard", "standard"), ("none", NO_PRESET)]:
            with self.subTest(given=given):
                args = merge_config_with_args(
                    build_parser().parse_args([]), {"preset": given})
                self.assertEqual(args.preset, expected)

    def test_config_preset_null_means_unset(self):
        args = merge_config_with_args(build_parser().parse_args([]), {"preset": None})
        self.assertIsNone(args.preset)

    def test_config_preset_empty_string_means_unset(self):
        """`"preset": ""` meant no preset before #137, so it still does."""
        for given in ["", " ", "\t\n"]:
            with self.subTest(given=given):
                args = merge_config_with_args(
                    build_parser().parse_args([]), {"preset": given})
                self.assertIsNone(args.preset)

    def test_spaces_are_stripped_in_the_config_file_but_not_on_the_command_line(self):
        args = merge_config_with_args(build_parser().parse_args([]), {"preset": " Strict "})
        self.assertEqual(args.preset, "strict")
        with patch("sys.stderr", new_callable=io.StringIO), self.assertRaises(SystemExit):
            build_parser().parse_args(["--preset", " strict "])

    def test_invalid_config_preset_is_an_error_that_lists_the_choices(self):
        choices = ", ".join(f"'{choice}'" for choice in PRESET_CHOICES)
        for given, shown in [("standrad", "'standrad'"), ("no ne", "'no ne'"),
                             (3, "'3' (a JSON number)"), (True, "'true' (a JSON boolean)"),
                             (False, "'false' (a JSON boolean)"), (0, "'0' (a JSON number)"),
                             (["standard"], """'["standard"]' (a JSON array)"""),
                             ({"name": "light"}, """'{"name": "light"}' (a JSON object)""")]:
            with self.subTest(given=given):
                with self.assertRaises(ValueError) as raised:
                    merge_config_with_args(build_parser().parse_args([]), {"preset": given})
                self.assertEqual(
                    str(raised.exception),
                    f"Invalid preset {shown} in the config file. "
                    f"Valid choices (in any letter case): {choices}.")

    def test_invalid_config_preset_error_names_the_config_file(self):
        with self.assertRaises(ValueError) as raised:
            merge_config_with_args(build_parser().parse_args([]), {"preset": "standrad"},
                                   Path(".foundationrc"))
        self.assertEqual(
            str(raised.exception),
            "Invalid preset 'standrad' in the config file '.foundationrc'. Valid choices "
            "(in any letter case): 'minimal', 'light', 'standard', 'strict', 'enterprise', "
            "'none'.")

    def test_invalid_config_preset_is_not_checked_when_the_command_line_overrides_it(self):
        args = merge_config_with_args(
            build_parser().parse_args(["--preset", "light"]), {"preset": "standrad"})
        self.assertEqual(args.preset, "light")

    def test_normalize_config_preset(self):
        self.assertEqual(normalize_config_preset(" Strict "), "strict")
        self.assertIsNone(normalize_config_preset(None))
        self.assertIsNone(normalize_config_preset(""))
        self.assertIsNone(normalize_config_preset("   "))

    def test_invalid_config_preset_error_escapes_control_characters(self):
        """A config file from a cloned repository must not send escapes to the terminal."""
        for given, shown in [("\x1b[31mred\x1b[0m", "'\\x1b[31mred\\x1b[0m'"),
                             ("standard\nError: forged", "'standard\\nError: forged'"),
                             ("a\rb\tc\x00d\x7fe", "'a\\rb\\tc\\x00d\\x7fe'"),
                             ("c1\x9b2J", "'c1\\x9b2J'"),
                             ("line\u2028break", "'line\\u2028break'"),
                             ("lone\ud800", "'lone\\ud800'")]:
            with self.subTest(given=given):
                with self.assertRaises(ValueError) as raised:
                    normalize_config_preset(given, Path(".foundationrc"))
                message = str(raised.exception)
                self.assertTrue(
                    message.startswith(f"Invalid preset {shown} in the config file "), message)
                self.assertTrue(message.isprintable(), message)
                for raw in ("\x1b", "\n", "\r", "\t", "\x00", "\x7f", "\x9b",
                            "\u2028", "\ud800"):
                    self.assertNotIn(raw, message)

    def test_invalid_config_preset_error_tells_a_backslash_from_an_escape(self):
        """A typed backslash and `n` must not look like an escaped line feed."""
        for given, shown in [("a\\nb", "'a\\\\nb'"),
                             ("a\nb", "'a\\nb'"),
                             ("a\\\nb", "'a\\\\\\nb'"),
                             ("C:\\x1b", "'C:\\\\x1b'")]:
            with self.subTest(given=given):
                with self.assertRaises(ValueError) as raised:
                    normalize_config_preset(given)
                self.assertIn(f"Invalid preset {shown} in the config file.",
                              str(raised.exception))

    def test_invalid_config_preset_error_keeps_printable_non_ascii_text(self):
        with self.assertRaises(ValueError) as raised:
            normalize_config_preset("st\u00e1ndard \u00e9 \u65e5\u672c")
        self.assertIn("Invalid preset 'st\u00e1ndard \u00e9 \u65e5\u672c' in the config file.",
                      str(raised.exception))

    def test_help_says_flags_add_to_a_preset_and_describes_none(self):
        help_text = build_parser().format_help()
        self.assertNotIn("Overrides individual", help_text)
        self.assertNotIn("same as leaving", help_text)
        preset_help = next(a.help for a in build_parser()._actions if a.dest == "preset")
        self.assertIn("'none' applies no preset", preset_help)
        self.assertIn("--include-* flags or --all given", preset_help)
        self.assertIn("overrides a preset set in the config file", preset_help)
        self.assertIn("any letter case", preset_help)

    def test_help_choices_stay_lowercase_and_examples_show_none(self):
        help_text = build_parser().format_help()
        self.assertIn("{" + ",".join(PRESET_CHOICES) + "}", help_text)
        self.assertIn("generate_foundation.py --preset none --include-ci", help_text)
        self.assertIn("enterprise, or none (no preset)", help_text)

    def test_help_says_a_broken_config_file_stops_the_run(self):
        help_text = build_parser().format_help()
        self.assertIn("foundationrc.json found in the current directory", help_text)
        self.assertIn("cannot be read, is not valid JSON, or\n  is not a JSON object", help_text)
        self.assertIn("stops the run with exit code 2", help_text)

    def test_config_file_accepts_none(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / ".foundationrc"
            config_path.write_text(json.dumps({"preset": "none"}))
            with patch("sys.stdout", new_callable=io.StringIO):
                config = load_config_file(str(config_path))
        args = build_parser().parse_args([])
        self.assertEqual(merge_config_with_args(args, config).preset, NO_PRESET)

    def test_include_option_help_lists_all_and_include_flags(self):
        options = dict(include_option_help())
        self.assertIn("--all", options)
        self.assertIn("--include-adr", options)
        self.assertTrue(all(o == "--all" or o.startswith("--include-") for o in options))
        self.assertTrue(all(options.values()))


class TestCommandLineOnlySettings(unittest.TestCase):
    """Accepting the agreement and overwriting files can't be set in a config file (#93, #113)."""

    def _args(self):
        return Namespace(project_name=None, author_name=None, license="mit",
                         non_interactive=False, accept_terms=False, force_overwrite=False)

    def test_accept_terms_in_config_is_ignored(self):
        for key in ("accept_terms", "accept-terms", "acceptTerms"):
            with self.subTest(key=key), patch("sys.stderr", new_callable=io.StringIO) as err:
                result = merge_config_with_args(self._args(), {key: True, "non_interactive": True})
                self.assertFalse(result.accept_terms)
                self.assertTrue(result.non_interactive)
                self.assertIn("--accept-terms", err.getvalue())

    def test_force_overwrite_in_config_is_ignored(self):
        for key in ("force_overwrite", "force-overwrite", "forceOverwrite"):
            with self.subTest(key=key), patch("sys.stderr", new_callable=io.StringIO) as err:
                result = merge_config_with_args(self._args(), {key: True})
                self.assertFalse(result.force_overwrite)
                self.assertIn("--force-overwrite", err.getvalue())

    def test_config_alone_cannot_pass_validation_in_non_interactive_mode(self):
        args = merge_config_with_args(
            Namespace(project_name=None, author_name=None, license="mit",
                      non_interactive=False, accept_terms=False, force_overwrite=False),
            {"project_name": "P", "author_name": "A", "non_interactive": True, "accept_terms": True})
        is_valid, message = validate_arguments(args)
        self.assertFalse(is_valid)
        self.assertIn("--accept-terms", message)


class TestValidateArguments(unittest.TestCase):
    """Test argument validation."""

    def test_valid_args_pass(self):
        """Valid arguments should pass validation."""
        args = Namespace(
            project_name="TestProject",
            author_name="Test Author",
            non_interactive=False,
            accept_terms=False,
        )
        is_valid, error = validate_arguments(args)
        self.assertTrue(is_valid)
        self.assertEqual(error, "")

    def test_missing_project_name_fails(self):
        """Missing project name should fail validation."""
        args = Namespace(
            project_name=None,
            author_name="Test Author",
            non_interactive=False,
            accept_terms=False,
        )
        is_valid, error = validate_arguments(args)
        self.assertFalse(is_valid)
        self.assertIn("project-name", error)

    def test_missing_author_name_fails(self):
        """Missing author name should fail validation."""
        args = Namespace(
            project_name="TestProject",
            author_name=None,
            non_interactive=False,
            accept_terms=False,
        )
        is_valid, error = validate_arguments(args)
        self.assertFalse(is_valid)
        self.assertIn("author-name", error)

    def test_non_interactive_requires_accept_terms(self):
        """Non-interactive mode requires accept-terms."""
        args = Namespace(
            project_name="TestProject",
            author_name="Test Author",
            non_interactive=True,
            accept_terms=False,
        )
        is_valid, error = validate_arguments(args)
        self.assertFalse(is_valid)
        self.assertIn("accept-terms", error)

    def test_non_interactive_with_accept_terms_passes(self):
        """Non-interactive mode with accept-terms should pass."""
        args = Namespace(
            project_name="TestProject",
            author_name="Test Author",
            non_interactive=True,
            accept_terms=True,
        )
        is_valid, error = validate_arguments(args)
        self.assertTrue(is_valid)


if __name__ == "__main__":
    unittest.main()
