import shutil

def open_file(input_arg):
    if input_arg[-1] == 'standard' or input_arg[-1] == 'shadow' or input_arg[-1] == 'thinkertoy':
        str1 = input_arg[-2]
        file = input_arg[-1]+'.txt'
    else:
        str1 = input_arg[-1]
        file = 'standard.txt'
    return (str1, file)

def output_flag_check(input_arg):
    for arg in input_arg:
        if '--output=' in arg:
            return arg.split('=')[1]
    return False

def color_flag(input_arg):
    color = None
    color_letter = ''
    ansi_colors ={
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'white': '\033[37m'
    }
    for i in range(len(input_arg)):
        if '--color=' in input_arg[i]:
            color = ansi_colors[input_arg[i].split('=')[1]]
            color_letter = input_arg[i+1]
    return (color, color_letter)

def justify(input_arg, str1):
    terminal_size = shutil.get_terminal_size().columns
    align = None
    count = 0
    for arg in input_arg:
        if '--align=' in arg:
            align = arg.split('=')[1]
    for i in list(str1):
        if i == 'm':
            count += 4
    if align == 'center':
        return str1.center(terminal_size + count)
    if align == 'right':
        return str1.rjust(terminal_size + count)
    if align == 'left':
        return str1.ljust(terminal_size + count)
    return str1