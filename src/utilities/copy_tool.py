import os
import subprocess
from .my_colors import colors

def copy_to_clipboard(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    subprocess.run('pbcopy', universal_newlines=True, input=file_content)
    print(f"{colors['light_green']}{os.path.basename(file_path)} content copied to clipboard.{colors['reset']}")
    return file_content

def copy_path_to_clipboard(path):
    subprocess.run('pbcopy', universal_newlines=True, input=path)
    print(f"{colors['light_green']}Path copied to clipboard: {path}{colors['reset']}")
    return path
