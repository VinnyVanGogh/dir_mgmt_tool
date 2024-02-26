import os

def find_closest_script(root_dir, script_name, default_ext):
    closest_match = None
    closest_distance = float('inf')
    script_name_lower = script_name.lower()

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            name, ext = os.path.splitext(filename.lower())
            if ext.lstrip(".").lower() == default_ext.lower():
                name = os.path.splitext(name)[0]

            if script_name_lower in name:
                distance = len(set(script_name_lower) ^ set(name))
                if distance < closest_distance:
                    closest_distance = distance
                    closest_match = os.path.join(dirpath, filename)

    return closest_match

