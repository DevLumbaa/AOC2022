import common
from itertools import islice

input_file = '\inputs\puzzle5.txt'
filename = common.get_inputs_directory(__file__, input_file)

super_list = []
# list_1 = ['Z', 'N']
# list_2 = ['M', 'C', 'D']
# list_3 = ['P']
# super_list = [list_1, list_2, list_3]

list_1 = ['T', 'D', 'W', 'Z', 'V', 'P']
list_2 = ['L','S','W', 'V', 'F', 'J', 'D']
list_3 = ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H']
list_4 = ['R','S','J']
list_5 = ['C','Z','B','G','F','M','L','W']
list_6 = ['Q','W','V','H','Z','R','G','B']
list_7 = ['V','J','P','C','B','D','N']
list_8 = ['P','T','B','Q']
list_9 = ['H','G','Z','R','C']
super_list = [list_1,list_2,list_3,list_4,list_5,list_6,list_7,list_8,list_9]

def move_stacks_1(number, source, target):
    for box in range(number):
        super_list[target-1].append(super_list[source-1][-1])
        super_list[source-1].pop()

def move_stacks_multiple(number, source, target):
    source_list_len = len(super_list[source-1])
    super_list[target-1].extend(super_list[source-1][-number:])
    del(super_list[source-1][-number:])

def comprehend_data(line):
    number = 0
    source = 0
    target = 0
    words = line.split()
    for index, word in enumerate(words):
        if(word == 'move'):
            number  = int(words[index+1])
        elif(word == 'from'):
            source  = int(words[index+1])
        elif(word == 'to'):
            target  = int(words[index+1])

    move_stacks_multiple(number, source, target)


with open(filename, 'r') as file:
    lines = file.readlines()
    line_count = 0
    list_stacks = []
    for line in lines:
        if(len(line.strip())!=0):
            line_count += 1
            list_stacks.append(line)
        else:
            break

    
    for line in islice(lines , line_count+1, None):
        comprehend_data(line)

    for sublist in super_list:
        #print(sublist)
        print(sublist[-1:])




