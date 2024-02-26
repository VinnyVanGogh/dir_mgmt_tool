import os
import subprocess
from ..settings.config import COLORS

def copy_to_clipboard(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    subprocess.run('pbcopy', universal_newlines=True, input=file_content)
    print(f"{COLORS['light_green']}{os.path.basename(file_path)} content copied to clipboard.{COLORS['reset']}")
    return file_content

def copy_path_to_clipboard(path):
    subprocess.run('pbcopy', universal_newlines=True, input=path)
    print(f"{path}")
    return path
