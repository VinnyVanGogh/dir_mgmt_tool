import sys
from src.settings.config import COLORS
from src.utilities.my_actions import print_error, confirm_action
from src.utilities.my_args import args
from src.utilities.my_handler import handle_find_script, handle_input_selection
from src.utilities.display_tool  import list_files, display_choices
from src.utilities.finder_tool import find_closest_script

def main():
    if args.script_path:
        script_path = find_closest_script(args.root_directory, args.script_path, args.extension)
        handle_find_script(script_path)
        sys.exit(0)
    current_dir = args.root_directory
    continue_loop = True
    while continue_loop:
        print(f"{COLORS['underline_text']}Current Directory: {current_dir} {COLORS['reset']}")
        sorted_items = list_files(current_dir)
        display_choices(sorted_items)
        choice = input(f"{COLORS['light_green']}?#Choose a folder or file:{COLORS['reset']} ")
        current_dir, continue_loop = handle_input_selection(choice, sorted_items, current_dir)

if __name__ == "__main__":
    main()
