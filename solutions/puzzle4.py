import common

input_file = '\inputs\puzzle4_dummy_data.txt'
filename = common.get_inputs_directory(__file__, input_file)

with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        print(data)
        for str in data:
            limits = set(str.split('-'))
            print(limits)

file.close()