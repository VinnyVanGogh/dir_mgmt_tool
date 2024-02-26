import os
from .my_colors import colors
from .my_actions import confirm_action, print_error

def delete_file(file_path):
    confirm_action("delete the file")
    os.remove(file_path)
    print(f"{colors['light_green']}Deleted {file_path}.{colors['reset']}")

def move_file(file_path, current_dir):
    confirm_action("move the file")
    new_location = input(f"Enter the new location for {os.path.basename(file_path)}: ")
    if not os.path.isdir(new_location):
        print_error("The specified location does not exist or is not a directory.")
        return current_dir
    new_path = os.path.join(new_location, os.path.basename(file_path))
    os.rename(file_path, new_path)
    print(f"{colors['light_green']}Moved to {new_path}.{colors['reset']}")
    return current_dir

