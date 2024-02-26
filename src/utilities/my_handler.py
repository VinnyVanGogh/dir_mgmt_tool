import os

from .copy_tool import copy_to_clipboard, copy_path_to_clipboard
from .change_tool import move_file, delete_file
from .manipulation_tool import edit_file, read_file, run_file
from .finder_tool import find_closest_script
from .display_tool import list_files, display_choices

from .my_actions import print_error, confirm_action
from .my_colors import colors
from .my_args import args

def handle_input_selection(choice, sorted_items, current_dir):
    total_items = len(sorted_items)

    try:
        choice = int(choice)
    except ValueError:
        print_error("Invalid selection. Try again.")
        return current_dir, True

    if choice == total_items + 1:
        return os.path.dirname(current_dir), True
    elif choice == total_items + 2:
        print_error("Exiting...")
        sys.exit(0)

    if 1 <= choice <= total_items:
        selected_item = sorted_items[choice - 1]
        _, item_name = selected_item.split(' ', 1)
        item_path = os.path.join(current_dir, item_name)

        if selected_item.startswith("[Folder]"):
            return item_path, True

        if args.edit_w_nvim and selected_item.startswith("[File]"):
            edit_file(item_path)
        elif args.read_file and selected_item.startswith("[File]"):
            read_file(item_path)
        elif args.copy_content and selected_item.startswith("[File]"):
            copy_to_clipboard(item_path)
        elif args.run_script and selected_item.startswith("[File]"):
            run_file(item_path)
        elif args.delete_file and selected_item.startswith("[File]"):
            delete_file(item_path)
        elif args.move_file and selected_item.startswith("[File]"):
            return move_file(item_path, current_dir), True

    else:
        print_error("Invalid selection. Try again.")
        return current_dir, True

    return current_dir, False

def handle_find_script(script_path):
    if args.script_path:
        if script_path:
            print(f"{colors['light_green']}Found closest match: {script_path}{colors['reset']}")
            if args.find_and_copy_path:
                copy_path_to_clipboard(script_path)
            elif args.copy_content:
                copy_to_clipboard(script_path)
            elif args.run_script:
                run_file(script_path)
            elif args.edit_w_nvim:
                edit_file(script_path)
            elif args.read_file:
                read_file(script_path)
            elif args.delete_file:
                delete_file(script_path)
            elif args.move_file:
                move_file(script_path, os.path.dirname(script_path))
        else:
            print_error("No matching script found.")
    else:
        print_error("Please specify a script name with --script.")
