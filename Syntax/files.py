input_file = open('file.txt', 'r')
i_f = input_file.readlines()
life_start_list = []


for line in i_f:
    life_start_list.append(list(line.strip()))

life_end_list = life_start_list

line_nr = -1
for life_line in life_start_list:
    line_nr = line_nr + 1
    for i in range(len(life_line)):
        if life_line[i] == '1':
            print(line_nr)
            life_end_list[line_nr][i-1] = '1'
            life_end_list[line_nr][i+1] = '1'
            life_end_list[line_nr-1][i] = '1'
            life_end_list[line_nr+1][i] = '1'

print(life_end_list)