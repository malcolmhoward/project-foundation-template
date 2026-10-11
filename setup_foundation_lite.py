#!/usr/bin/env python3
"""
Project Foundation Generator - legacy entry point (deprecated)

WHAT: A compatibility shim: a small stand-in file that keeps an old command working by
forwarding to the code that replaced it (see GLOSSARY.md). `setup_foundation_lite.py` was
the single-file generator through v2.5.x. Since v2.6.0 the generator lives in the `core/`
package, and since v3.0.0 the entry point is `generate_foundation.py`. This file runs exactly
that generator, with the same arguments, so existing scripts and CI jobs keep working.

WHY: Removing a documented entry point breaks people's automation without warning. Keeping a
thin shim (rather than a second copy of the generator) means there is one implementation to
maintain, and the shim can never drift from it.

HOW: Replace `python setup_foundation_lite.py ...` with `python generate_foundation.py ...`.
The shim needs the `core/` package beside it: downloading this one file on its own no longer
works (see MIGRATION.md, "From Lite v2.5.x to v2.6.0").

Copyright (c) 2025 Malcolm Howard

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Repository: https://github.com/malcolmhoward/project-foundation-template
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    import generate_foundation
except ImportError as exc:
    print(f"""
ERROR: setup_foundation_lite.py could not load the generator ({exc}).

Since v2.6.0 this file only forwards to the generator in the `core/` package, so it needs
the full repository, not this single file. Clone the repository and run:

    python generate_foundation.py --project-name "MyProject" --author-name "Your Name"

See MIGRATION.md ("From Lite v2.5.x to v2.6.0") for details.
""", file=sys.stderr)
    sys.exit(1)


DEPRECATION_NOTICE = (
    "Note: setup_foundation_lite.py is deprecated and will be removed in a future major release.\n"
    "      It runs generate_foundation.py with the same arguments; please call that directly.\n"
)


def main() -> int:
    """Print a deprecation notice (unless quiet), then run the current generator."""
    if not any(flag in sys.argv[1:] for flag in ("--quiet", "--version", "-h", "--help")):
        print(DEPRECATION_NOTICE, file=sys.stderr)
    return generate_foundation.main()


if __name__ == "__main__":
    sys.exit(main())
