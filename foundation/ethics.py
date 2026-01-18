# foundation/ethics.py
# Ethics-related functionality and safeguards

"""
Ethics module for Project Foundation Template.

Contains:
    - Version expiration advisory checks
    - Ethical use agreement display and acknowledgment
    - Helper functions for ethical safeguards

These functions provide the ethical guardrails for the template generator,
ensuring users understand the limitations and responsibilities of using
generated templates.
"""

import time
from datetime import date

from foundation.utils import EXPIRATION_DATE, OFFICIAL_REPO
from foundation.education import ETHICAL_USE_AGREEMENT


def check_version_advisory(
    expiration_date: date = None,
    is_interactive: bool = True,
    is_quiet: bool = False,
    input_func=None,
    print_func=None
) -> bool:
    """
    Advisory version check - warns but doesn't block.

    This function checks if the current version has expired and handles
    the user interaction appropriately based on the mode (interactive vs
    non-interactive, quiet vs verbose).

    Args:
        expiration_date: The date when this version expires. Defaults to
                        EXPIRATION_DATE from utils module.
        is_interactive: Whether running in interactive mode (prompts for input).
        is_quiet: Whether to suppress non-essential output.
        input_func: Optional custom input function (for testing). Defaults to builtin input.
        print_func: Optional custom print function (for testing). Defaults to builtin print.

    Returns:
        True if the user can proceed (not expired or acknowledged risk),
        False if the user declined to continue with an expired version.

    Example:
        >>> # In non-interactive CI mode
        >>> check_version_advisory(is_interactive=False, is_quiet=True)
        True

        >>> # In interactive mode with unexpired version
        >>> check_version_advisory(is_interactive=True)
        True
    """
    if expiration_date is None:
        expiration_date = EXPIRATION_DATE

    if input_func is None:
        input_func = input

    if print_func is None:
        print_func = print

    if date.today() > expiration_date:
        if not is_quiet:
            print_func(f"""
\u26a0\ufe0f  VERSION OUTDATED - SECURITY RISK

This version expired on {expiration_date.isoformat()}.
Security practices and compliance requirements have likely changed.

Using outdated templates may introduce vulnerabilities or compliance issues.

Get the latest version at: {OFFICIAL_REPO}

""")

        if is_interactive:
            response = input_func("Type 'I understand the risks' to continue anyway: ")
            if response.strip() != "I understand the risks":
                print_func("\u274c Exiting for your safety. Please get the latest version.")
                return False
            print_func("\u26a0\ufe0f  Proceeding with outdated version at your own risk.\n")
        else:
            # Non-interactive mode: warn but continue (user accepted terms)
            if not is_quiet:
                print_func("\u26a0\ufe0f  Non-interactive mode: Proceeding with outdated version.\n")

    return True


def show_ethical_agreement(
    is_interactive: bool = True,
    is_quiet: bool = False,
    input_func=None,
    print_func=None,
    sleep_func=None
) -> bool:
    """
    Display ethical use agreement and get acknowledgment.

    This function presents the ethical use agreement to users and requires
    acknowledgment before proceeding. In non-interactive mode, it assumes
    terms were pre-accepted via --accept-terms flag.

    Args:
        is_interactive: Whether running in interactive mode (requires user input).
        is_quiet: Whether to suppress non-essential output.
        input_func: Optional custom input function (for testing). Defaults to builtin input.
        print_func: Optional custom print function (for testing). Defaults to builtin print.
        sleep_func: Optional custom sleep function (for testing). Defaults to time.sleep.

    Returns:
        True if the user agreed to the terms (or is in non-interactive mode),
        False if the user declined the terms.

    Example:
        >>> # Non-interactive mode (CI/automation)
        >>> show_ethical_agreement(is_interactive=False)
        True

        >>> # Interactive mode (mocked for testing)
        >>> def mock_input(prompt): return "yes"
        >>> show_ethical_agreement(is_interactive=True, input_func=mock_input)
        True
    """
    if input_func is None:
        input_func = input

    if print_func is None:
        print_func = print

    if sleep_func is None:
        sleep_func = time.sleep

    # In non-interactive mode, terms are pre-accepted via --accept-terms
    if not is_interactive:
        if not is_quiet:
            print_func("\u2713 Ethical use agreement accepted via --accept-terms flag.\n")
        return True

    print_func(ETHICAL_USE_AGREEMENT)

    # Force them to read it
    for i in range(3, 0, -1):
        print_func(f"\rPlease read the agreement carefully... {i}", end="")
        sleep_func(1)
    print_func("\n")

    response = input_func("Do you understand and agree to these terms? (yes/no): ")
    if response.lower() != "yes":
        print_func("\u274c You must agree to the ethical use terms to continue.")
        return False

    # Second confirmation for emphasis
    response = input_func("Will you customize these templates for your specific needs? (yes/no): ")
    if response.lower() != "yes":
        print_func("\u274c Templates MUST be customized. They are not complete solutions.")
        return False

    return True


def is_version_expired(expiration_date: date = None) -> bool:
    """
    Check if the current version has expired.

    This is a simple helper that checks if today's date is past the
    expiration date. Unlike check_version_advisory, this does not
    handle any user interaction - it simply returns the expiration status.

    Args:
        expiration_date: The date when this version expires. Defaults to
                        EXPIRATION_DATE from utils module.

    Returns:
        True if the version has expired, False otherwise.

    Example:
        >>> from datetime import date
        >>> is_version_expired(date(2020, 1, 1))  # Past date
        True
        >>> is_version_expired(date(2099, 1, 1))  # Future date
        False
    """
    if expiration_date is None:
        expiration_date = EXPIRATION_DATE

    return date.today() > expiration_date


def get_version_status(expiration_date: date = None) -> dict:
    """
    Get comprehensive version status information.

    Returns a dictionary containing version expiration status, days until
    expiration (or days since), and the expiration date.

    Args:
        expiration_date: The date when this version expires. Defaults to
                        EXPIRATION_DATE from utils module.

    Returns:
        Dictionary with keys:
            - is_expired: bool - Whether the version has expired
            - expiration_date: date - The expiration date
            - days_remaining: int - Days until expiration (negative if expired)
            - status: str - Human-readable status ("valid", "expiring_soon", "expired")

    Example:
        >>> status = get_version_status()
        >>> status['is_expired']
        False
        >>> status['status']
        'valid'
    """
    if expiration_date is None:
        expiration_date = EXPIRATION_DATE

    today = date.today()
    days_remaining = (expiration_date - today).days
    is_expired = days_remaining < 0

    if is_expired:
        status = "expired"
    elif days_remaining <= 30:
        status = "expiring_soon"
    else:
        status = "valid"

    return {
        "is_expired": is_expired,
        "expiration_date": expiration_date,
        "days_remaining": days_remaining,
        "status": status
    }
