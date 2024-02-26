from .my_colors import colors

def print_error(message):
    print(f"{colors['red']}{message}{colors['reset']}")

def confirm_action(message):
    confirmation = input(f"Are you sure you want to {message}? (y/n): ")
    if confirmation.lower() != "y":
        print(f"{colors['light_green']}Copy to clipboard cancelled.{colors['reset']}")
        return

