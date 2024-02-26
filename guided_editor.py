import subprocess
from colorama import Fore, Style, init
import argparse

parser = argparse.ArgumentParser(description="Guided editor for file manipulation")
parser.add_argument("-skip", action="store_true", help="Skip the y/n questions and directly ask for input values")
args = parser.parse_args()

input_options = {}

colors = {
    'green': Fore.GREEN,
    'red': Fore.RED,
    'yellow': Fore.YELLOW,
    'pink': Fore.MAGENTA,
    'blue': Fore.BLUE,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE,
    'orange': Fore.LIGHTYELLOW_EX,
    'new_pink': Fore.LIGHTRED_EX,
    'lilac': Fore.LIGHTBLUE_EX,
    'reset': Style.RESET_ALL
}

reset = colors['reset']

init(autoreset=True)

actions_dict = {
    'copy': '-copy',
    'delete': '-delete',
    'move': '-move',
    'run': '-run',
    'copy_path': '-find',
    'read': '-read'
}


def ask_for_input(prompt, key, options_dict, input_color):
    if args.skip:
        options_dict[key] = input(f"{input_color}Enter the {prompt}: {reset}")
    else:
        consent = input(f"{input_color}Do you want to enter {prompt}? (y/n): {reset}").strip().lower()
        if consent == 'y':
            options_dict[key] = input(f"{input_color}Enter the {prompt}: {reset}")
        elif consent == 'n':
            options_dict[key] = None

def ask_for_action(actions_dict):
    print(f"{colors['green']}Available actions:")
    for i, action in enumerate(actions_dict, start=1):
        print(f"{colors['pink']}{i}) {action}")

    try:
        choice = int(input(f"{colors['lilac']}Select an action by its number: {reset}")) - 1
        action_keys = list(actions_dict.keys())
        if choice >= 0 and choice < len(action_keys):
            selected_action_key = action_keys[choice]
            selected_action_value = actions_dict[selected_action_key]
            return selected_action_value
        else:
            print(f"{input_color}Invalid selection. Please enter a number from the list.{reset}")
            return None
    except ValueError:
        print(f"{input_color}Invalid input. Please enter a numeric value.{reset}")
        return None


def validate_input(input_key, options_dict):
    return options_dict.get(input_key) == 'y'

def construct_command(input_options, selected_action):
    command = ["python3 /Users/vincevasile/Documents/DEV/PYTHON/new_scripts/file_manipulation/copy_and_edit/master_editor.py"]
    
    if input_options.get('file_extension'):
        command.append(f"-ext {input_options['file_extension']}")
    
    if input_options.get('directory'):
        command.append(f"-root \"{input_options['directory']}\"")
    
    if input_options.get('script_name'):
        command.append(f"-script {input_options['script_name']}")

    if args.skip:
        command.append("-skip")
    
    if selected_action:
        command.append(selected_action)
    
    return ' '.join(command)

def main():
    ask_for_input("file extension", 'file_extension', input_options, colors['pink'])
    ask_for_input("directory to start the search from", 'directory', input_options, colors['lilac'])
    ask_for_input("name (or a partial name) of the script (no extension)", 'script_name', input_options, colors['new_pink'])

    extension = (input_options['file_extension'])
    directory = (input_options['directory'])
    script_name = (input_options['script_name'])

    selected_action = ask_for_action(actions_dict)

    final_command = construct_command(input_options, selected_action)

    print(f"{colors['pink']}Command to be executed: {final_command}{colors['reset']}{colors['new_pink']}")

    subprocess.run(final_command, shell=True)

if __name__ == '__main__':
    main()
