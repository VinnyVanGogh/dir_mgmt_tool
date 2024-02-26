import os
from ..settings.config import COLORS
from .my_args import args

def list_files(current_dir):
    items = []
    for entry in os.listdir(current_dir):
        full_path = os.path.join(current_dir, entry)
        if os.path.isdir(full_path):
            items.append(f"[Folder] {entry}")
        elif os.path.isfile(full_path) and full_path.endswith(f".{args.extension}"):
            items.append(f"[File] {entry}")
    return sorted(items)

def display_choices(sorted_items):
    idx = 1
    for item in sorted_items:
        label, name = item.split(' ', 1)
        color = COLORS["orange"] if "[Folder]" in label else COLORS["cyan"]
        print(f"{color}{idx}) {label}{COLORS['reset']} {name}")
        idx += 1
    print(f"{COLORS['pink']}{idx}) Go back{COLORS['reset']}")
    idx += 1
    print(f"{COLORS['red']}{idx}) Exit{COLORS['reset']}")

