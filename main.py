import sys
from functions import open_file, output_flag_check, color_flag, justify

#go through file and find letter
def read_file(str1, file, color, color_letter):
    d = {}
    lines = []
    opt = 0
    counter = opt
    for ch in range(len(str1)):
        if str1[ch] == '\\' and str1[ch + 1] == 'n':
            opt += 8
            counter = opt
            continue
        if str1[ch-1] == '\\' and str1[ch] == 'n':
            continue
        start_line = (ord(str1[ch]) - 32) * 8 + (ord(str1[ch]) - 30)
        file.seek(0)
        for line_number, line in enumerate(file, start=1):
            if line_number in range(start_line, start_line + 9):
                counter += 1
                if str1[ch] in color_letter:
                    lines = color + line[:-1] + '\033[0m'
                else:
                    lines = line[:-1]
                d[counter] = d.get(counter, '') + lines
        counter = opt
    
    file.close()
    return d
    

#output flag check
output_file_name = output_flag_check(sys.argv)
output_file = open(output_file_name, 'w')

#open file
str1, banner_name = open_file(sys.argv)
file = open(banner_name, 'r')

#check --color flag and get corresponding color and letters
color, color_letter = color_flag(sys.argv)

output = read_file(str1, file, color, color_letter)

if output_file_name == False:
    for i, j in output.items():
        print(justify(sys.argv, j))
else:
    for i, j in output.items():
        output_file.write(justify(sys.argv, j) + '\n')
    output_file.close()

