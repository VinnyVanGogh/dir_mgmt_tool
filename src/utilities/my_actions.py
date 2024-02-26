from ..settings.config import COLORS
from .my_args import args

def print_error(message):
    print(f"{COLORS['red']}{message}{COLORS['reset']}")

def confirm_action(message):
    if args.skip_confirmation:
        return
    confirmation = input(f"Are you sure you want to {message}? (y/n): ")
    if confirmation.lower() != "y":
        print(f"{COLORS['light_green']}Copy to clipboard cancelled.{COLORS['reset']}")
        return

