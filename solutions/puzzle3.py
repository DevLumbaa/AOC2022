import os
from pathlib import Path
import string

cur_dir, _ = os.path.split(os.path.abspath(__file__))
filename =  str((Path(cur_dir).parents[0])) + '\inputs\puzzle3_dummy_data.txt'

list_letters = list(string.ascii_letters)
list_points = list(range(1,53,1))
letter_point_dict = dict(zip(list_letters, list_points))
print(letter_point_dict)

with open(filename, 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        data = line.strip()
        firstpart, secondpart = data[:len(data)//2], data[len(data)//2:]
        print(firstpart, secondpart)

file.close()