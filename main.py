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
                lines = list(line)[:-1]
                if str1[ch] in color_letter:
                    for i in range(len(lines)):
                        lines[i] = color + lines[i] + '\033[0m'
                d[counter] = d.get(counter, []) + lines
        counter = opt
    
    file.close()
    return d
    

#output flag check
output_file = output_flag_check(sys.argv)

#open file
str1, file = open_file(sys.argv)

#check --color flag and get corresponding color and letters
color, color_letter = color_flag(sys.argv)

output = read_file(str1, file, color, color_letter)

if output_file == False:
    for i, j in output.items():
        print(justify(sys.argv, ''.join(j)))
else:
    for i, j in output.items():
        output_file.write(''.join(j) + '\n')
    output_file.close()
