# tests/test_foundation_ethics.py
# Unit tests for foundation/ethics.py

"""Unit tests for the foundation.ethics module."""

import unittest
from datetime import date, timedelta
from unittest.mock import MagicMock

<<<<<<< HEAD
from core.ethics import (
=======
from foundation.ethics import (
>>>>>>> 2d1b774 (refactor(v3.0.0): Phase 1 - Extract generator and ethics modules)
    check_version_advisory,
    show_ethical_agreement,
    is_version_expired,
    get_version_status,
)


class TestIsVersionExpired(unittest.TestCase):
    """Test is_version_expired helper function."""

    def test_returns_true_for_past_date(self):
        """Should return True when expiration date is in the past."""
        past_date = date.today() - timedelta(days=1)
        self.assertTrue(is_version_expired(past_date))

    def test_returns_false_for_future_date(self):
        """Should return False when expiration date is in the future."""
        future_date = date.today() + timedelta(days=30)
        self.assertFalse(is_version_expired(future_date))

    def test_returns_false_for_today(self):
        """Should return False when expiration date is today (not yet expired)."""
        today = date.today()
        self.assertFalse(is_version_expired(today))

    def test_uses_default_expiration_date(self):
        """Should use default expiration date when none provided."""
        # Just verify it doesn't raise an error
        result = is_version_expired()
        self.assertIsInstance(result, bool)


class TestGetVersionStatus(unittest.TestCase):
    """Test get_version_status helper function."""

    def test_returns_dict_with_required_keys(self):
        """Should return dict with all required keys."""
        status = get_version_status()
        required_keys = ["is_expired", "expiration_date", "days_remaining", "status"]
        for key in required_keys:
            self.assertIn(key, status)

    def test_expired_status_for_past_date(self):
        """Should return expired status for past date."""
        past_date = date.today() - timedelta(days=10)
        status = get_version_status(past_date)
        self.assertTrue(status["is_expired"])
        self.assertEqual(status["status"], "expired")
        self.assertLess(status["days_remaining"], 0)

    def test_valid_status_for_future_date(self):
        """Should return valid status for date more than 30 days away."""
        future_date = date.today() + timedelta(days=60)
        status = get_version_status(future_date)
        self.assertFalse(status["is_expired"])
        self.assertEqual(status["status"], "valid")
        self.assertGreater(status["days_remaining"], 30)

    def test_expiring_soon_status(self):
        """Should return expiring_soon status for date within 30 days."""
        soon_date = date.today() + timedelta(days=15)
        status = get_version_status(soon_date)
        self.assertFalse(status["is_expired"])
        self.assertEqual(status["status"], "expiring_soon")
        self.assertGreater(status["days_remaining"], 0)
        self.assertLessEqual(status["days_remaining"], 30)

    def test_expiration_date_in_result(self):
        """Should include the expiration date in result."""
        test_date = date(2025, 12, 31)
        status = get_version_status(test_date)
        self.assertEqual(status["expiration_date"], test_date)


class TestCheckVersionAdvisory(unittest.TestCase):
    """Test check_version_advisory function."""

    def test_returns_true_for_valid_version(self):
        """Should return True when version is not expired."""
        future_date = date.today() + timedelta(days=30)
        result = check_version_advisory(
            expiration_date=future_date,
            is_interactive=True,
            is_quiet=True
        )
        self.assertTrue(result)

    def test_returns_true_for_expired_non_interactive(self):
        """Should return True for expired version in non-interactive mode."""
        past_date = date.today() - timedelta(days=1)
        mock_print = MagicMock()
        result = check_version_advisory(
            expiration_date=past_date,
            is_interactive=False,
            is_quiet=False,
            print_func=mock_print
        )
        self.assertTrue(result)
        # Should have printed warning
        self.assertTrue(mock_print.called)

    def test_returns_true_for_expired_quiet_non_interactive(self):
        """Should return True silently for expired version in quiet non-interactive mode."""
        past_date = date.today() - timedelta(days=1)
        mock_print = MagicMock()
        result = check_version_advisory(
            expiration_date=past_date,
            is_interactive=False,
            is_quiet=True,
            print_func=mock_print
        )
        self.assertTrue(result)

    def test_returns_true_when_user_accepts_risk(self):
        """Should return True when user types 'I understand the risks'."""
        past_date = date.today() - timedelta(days=1)
        mock_input = MagicMock(return_value="I understand the risks")
        mock_print = MagicMock()
        result = check_version_advisory(
            expiration_date=past_date,
            is_interactive=True,
            is_quiet=False,
            input_func=mock_input,
            print_func=mock_print
        )
        self.assertTrue(result)
        mock_input.assert_called_once()

    def test_returns_false_when_user_declines(self):
        """Should return False when user doesn't accept risk."""
        past_date = date.today() - timedelta(days=1)
        mock_input = MagicMock(return_value="no")
        mock_print = MagicMock()
        result = check_version_advisory(
            expiration_date=past_date,
            is_interactive=True,
            is_quiet=False,
            input_func=mock_input,
            print_func=mock_print
        )
        self.assertFalse(result)

    def test_prints_warning_for_expired_version(self):
        """Should print warning message when version is expired."""
        past_date = date.today() - timedelta(days=1)
        mock_print = MagicMock()
        check_version_advisory(
            expiration_date=past_date,
            is_interactive=False,
            is_quiet=False,
            print_func=mock_print
        )
        # Check that the warning was printed
        call_args = mock_print.call_args_list
        warning_printed = any("OUTDATED" in str(call) or "expired" in str(call) for call in call_args)
        self.assertTrue(warning_printed)

    def test_no_warning_for_valid_version(self):
        """Should not print warning when version is valid."""
        future_date = date.today() + timedelta(days=30)
        mock_print = MagicMock()
        check_version_advisory(
            expiration_date=future_date,
            is_interactive=True,
            is_quiet=False,
            print_func=mock_print
        )
        self.assertFalse(mock_print.called)


class TestShowEthicalAgreement(unittest.TestCase):
    """Test show_ethical_agreement function."""

    def test_returns_true_for_non_interactive(self):
        """Should return True in non-interactive mode (terms pre-accepted)."""
        result = show_ethical_agreement(
            is_interactive=False,
            is_quiet=True
        )
        self.assertTrue(result)

    def test_prints_message_for_non_interactive_verbose(self):
        """Should print acceptance message in non-interactive verbose mode."""
        mock_print = MagicMock()
        show_ethical_agreement(
            is_interactive=False,
            is_quiet=False,
            print_func=mock_print
        )
        mock_print.assert_called()
        call_args_str = str(mock_print.call_args_list)
        self.assertIn("accepted", call_args_str)

    def test_returns_true_when_user_agrees(self):
        """Should return True when user agrees to terms."""
        mock_input = MagicMock(return_value="yes")
        mock_print = MagicMock()
        mock_sleep = MagicMock()
        result = show_ethical_agreement(
            is_interactive=True,
            is_quiet=False,
            input_func=mock_input,
            print_func=mock_print,
            sleep_func=mock_sleep
        )
        self.assertTrue(result)
        # Should have called input twice (terms + customization)
        self.assertEqual(mock_input.call_count, 2)

    def test_returns_false_when_user_declines_terms(self):
        """Should return False when user declines terms."""
        mock_input = MagicMock(return_value="no")
        mock_print = MagicMock()
        mock_sleep = MagicMock()
        result = show_ethical_agreement(
            is_interactive=True,
            is_quiet=False,
            input_func=mock_input,
            print_func=mock_print,
            sleep_func=mock_sleep
        )
        self.assertFalse(result)
        # Should have only called input once (stopped after first decline)
        self.assertEqual(mock_input.call_count, 1)

    def test_returns_false_when_user_wont_customize(self):
        """Should return False when user won't customize templates."""
        # First input: yes (agrees to terms)
        # Second input: no (won't customize)
        mock_input = MagicMock(side_effect=["yes", "no"])
        mock_print = MagicMock()
        mock_sleep = MagicMock()
        result = show_ethical_agreement(
            is_interactive=True,
            is_quiet=False,
            input_func=mock_input,
            print_func=mock_print,
            sleep_func=mock_sleep
        )
        self.assertFalse(result)
        # Should have called input twice
        self.assertEqual(mock_input.call_count, 2)

    def test_displays_agreement_in_interactive_mode(self):
        """Should display the ethical use agreement in interactive mode."""
        mock_input = MagicMock(return_value="yes")
        mock_print = MagicMock()
        mock_sleep = MagicMock()
        show_ethical_agreement(
            is_interactive=True,
            is_quiet=False,
            input_func=mock_input,
            print_func=mock_print,
            sleep_func=mock_sleep
        )
        # Check that agreement was printed (contains key phrases)
        all_calls = str(mock_print.call_args_list)
        self.assertIn("ETHICAL USE AGREEMENT", all_calls)

    def test_forces_reading_delay(self):
        """Should force a reading delay in interactive mode."""
        mock_input = MagicMock(return_value="yes")
        mock_print = MagicMock()
        mock_sleep = MagicMock()
        show_ethical_agreement(
            is_interactive=True,
            is_quiet=False,
            input_func=mock_input,
            print_func=mock_print,
            sleep_func=mock_sleep
        )
        # Should have called sleep 3 times (countdown 3, 2, 1)
        self.assertEqual(mock_sleep.call_count, 3)

    def test_case_insensitive_yes(self):
        """Should accept 'YES', 'Yes', etc."""
        mock_input = MagicMock(return_value="YES")
        mock_print = MagicMock()
        mock_sleep = MagicMock()
        result = show_ethical_agreement(
            is_interactive=True,
            is_quiet=False,
            input_func=mock_input,
            print_func=mock_print,
            sleep_func=mock_sleep
        )
        self.assertTrue(result)


class TestIntegration(unittest.TestCase):
    """Integration tests for ethics module functions."""

    def test_functions_importable_from_foundation(self):
<<<<<<< HEAD
        """Should be able to import ethics functions from core package."""
        from core import (
=======
        """Should be able to import ethics functions from foundation package."""
        from foundation import (
>>>>>>> 2d1b774 (refactor(v3.0.0): Phase 1 - Extract generator and ethics modules)
            check_version_advisory,
            show_ethical_agreement,
            is_version_expired,
            get_version_status,
        )
        # Just verify they're callable
        self.assertTrue(callable(check_version_advisory))
        self.assertTrue(callable(show_ethical_agreement))
        self.assertTrue(callable(is_version_expired))
        self.assertTrue(callable(get_version_status))

    def test_version_status_consistent_with_is_expired(self):
        """get_version_status and is_version_expired should be consistent."""
        test_dates = [
            date.today() - timedelta(days=30),  # expired
            date.today() + timedelta(days=30),  # valid
            date.today() + timedelta(days=15),  # expiring soon
        ]
        for test_date in test_dates:
            status = get_version_status(test_date)
            expired = is_version_expired(test_date)
            self.assertEqual(
                status["is_expired"],
                expired,
                f"Inconsistent result for date {test_date}"
            )


if __name__ == "__main__":
    unittest.main()
