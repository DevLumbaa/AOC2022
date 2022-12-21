import common

input_file = '\inputs\puzzle4.txt'
filename = common.get_inputs_directory(__file__, input_file)

def compare_pairs(pair1, pair2):
    count = 0
    lower_limit1 = int(pair1[0])
    upper_limit1 = int(pair1[1])
    lower_limit2 = int(pair2[0])
    upper_limit2 = int(pair2[1])
    if(lower_limit1 <= lower_limit2 and upper_limit1 >= upper_limit2):
        count = 1
    elif(lower_limit2 <= lower_limit1 and upper_limit2 >= upper_limit1):
        count = 1
    return count

def overlapping_pairs(pair1, pair2):
    count = 0
    lower_limit1 = int(pair1[0])
    upper_limit1 = int(pair1[1])
    lower_limit2 = int(pair2[0])
    upper_limit2 = int(pair2[1])
    if(lower_limit2 <= upper_limit1 and lower_limit2>=lower_limit1):
        count = 1
    elif(lower_limit1 <= upper_limit2 and lower_limit1>=lower_limit2):
        count = 1
    return count


with open(filename, 'r') as file:
    lines = file.readlines()
    count = 0
    for line in lines:
        data = line.strip().split(',')
        # print(data[0].split('-'), data[1].split('-'))
        pair1 = data[0].split('-')
        pair2 = data[1].split('-')
        #count += compare_pairs(pair1, pair2)
        count += overlapping_pairs(pair1, pair2)


    print('number of overlapping pairs = ',count)

file.close()