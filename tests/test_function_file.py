import shutil
import sys
sys.path.append('/home/user/projects/ascii-art-project-1-Kamila3361')

from functions import open_file, output_flag_check, color_flag, justify

def test_open_file():
    assert open_file(['main.py', 'Hello']) == ('Hello', 'standard.txt')
    assert open_file(['main.py', 'Hello', 'shadow']) == ('Hello', 'shadow.txt')
    assert open_file(['main.py', 'Hello', 'thinkertoy']) == ('Hello', 'thinkertoy.txt')
    assert open_file(['main.py', 'Hello', 'standard']) == ('Hello', 'standard.txt')


def test_output_flag_check():
    assert output_flag_check(['main.py', 'Hello', 'standard']) == False
    assert output_flag_check(['main.py', '--output=banner.txt', 'Hello', 'standard']) == 'banner.txt'


def test_color_flag():
    assert color_flag(['main.py', 'Hello', 'standard']) == (None, '')
    assert color_flag(['main.py', '--color=red', 'Hello', 'standard']) == ('\033[31m', 'Hello')
    assert color_flag(['main.py', '--color=red', 'Hell', 'Hello', 'standard']) == ('\033[31m', 'Hell')


def test_justify():
    terminal_size = shutil.get_terminal_size().columns
    assert justify(['main.py', 'Hello', 'standard'], 'String') == 'String'
    assert justify(['main.py', '--align=center', 'Hello'], 'String') == 'String'.center(terminal_size)
    assert justify(['main.py', '--align=right', 'Hello'], 'String') == 'String'.rjust(terminal_size)
    assert justify(['main.py', '--align=left', 'Hello'], 'String') == 'String'.ljust(terminal_size)
    assert justify(['main.py', '--align=center', '--color=red', 'Hello'], 'String') == 'String'.center(terminal_size)