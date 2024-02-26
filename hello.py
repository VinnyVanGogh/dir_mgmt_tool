from src.utilities.my_colors import colors

def say_hello():
    first_line = f"{colors['red']}Hello, World!"
    second_line = f"{colors['light_green']}I am a Python program."
    print(first_line)
    print(second_line)

say_hello()
