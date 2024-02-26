import subprocess
from .my_actions import confirm_action, print_error
from ..settings.config import COLORS

def edit_file(file_path):
    print(f"{COLORS['light_green']}Opening {file_path} in NeoVim...{COLORS['reset']}")
    subprocess.call(['nvim', file_path])

def read_file(file_path):
    try:
        subprocess.run(['bat', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print_error(f"Error: {e}.")
    except FileNotFoundError:
        try:
            with open(file_path, 'r') as file:
                print(file.read())
        except Exception as e:
            error_message = f"Error reading file: {e}."
            print_error(error_message)
    except Exception as e:
        error_message = f"Unexpected error: {e}."
        print_error(error_message)

def run_file(file_path):
    confirm_action("run the file")
    script_modes = {"sh": "bash", "py": "python3", "zsh": "zsh"}
    extension = file_path.split('.')[-1]
    if extension in script_modes:
        subprocess.run([script_modes[extension], file_path])

