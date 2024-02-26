import argparse
from ..settings.config import DEFAULTS

def parse_args():
    parser = argparse.ArgumentParser(description='A versatile script handling various file operations.')
    parser.add_argument('-root', '--root_directory', type=str, default=DEFAULTS["root"], help='Root directory to search for files in.')
    parser.add_argument('-ext', '--extension', type=str, default=DEFAULTS["ext"], help='File extension to search for.')
    parser.add_argument('-edit', '--edit_w_nvim', action='store_true', help='Edit file mode with nvim')
    parser.add_argument('-read', '--read_file', action='store_true', help='Read file mode (bat or cat file')
    parser.add_argument('-copy', '--copy_content', action='store_true', help='Copy file content to clipboard with pbcopy')
    parser.add_argument('-run', '--run_script', action='store_true', help='Run file as a script based on the extension')
    parser.add_argument('-delete', '--delete_file', action='store_true', help='Delete file with confirmation')
    parser.add_argument('-move', '--move_file', action='store_true', help='Move file mode with confirmation')
    parser.add_argument('-script', '--script_path', type=str, help='Script name to find and operate on in the root directory')
    parser.add_argument('-find', '--find_and_copy_path', action='store_true', help='Find and copy script path to clipboard searches from root directory down')
    parser.add_argument('-skip', '--skip_confirmation', action='store_true', help='Skip confirmation for delete and move operations')
    return parser.parse_args()

args = parse_args()
