import os
from pathlib import Path
import string

cur_dir, _ = os.path.split(os.path.abspath(__file__))
filename =  str((Path(cur_dir).parents[0])) + '\inputs\puzzle3.txt'

list_letters = list(string.ascii_letters)
list_points = list(range(1,53,1))
letter_point_dict = dict(zip(list_letters, list_points))

with open(filename, 'r') as file:
    lines = file.read().splitlines()
    points = 0
    for line in lines:
        data = line.strip()
        firstpart, secondpart = data[:len(data)//2], data[len(data)//2:]
        misplaced_itmes = set.intersection(set(firstpart),set(secondpart))
        for item in misplaced_itmes:
            points += letter_point_dict.get(item)
    
    print(points)

file.close()