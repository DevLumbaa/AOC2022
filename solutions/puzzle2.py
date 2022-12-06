import re
import os
from pathlib import Path

cur_dir, _ = os.path.split(os.path.abspath(__file__))
# print(cur_dir)
filename =  str((Path(cur_dir).parents[0])) + '\inputs\puzzle2.txt'
# print(filename)

#A=X=ROCK
#B=Y=PAPER
#C=Z=SCISSORS

#part2
#x = lose
#y = draw
#z = win

list1 = ['A', 'B', 'C']
list2 = ['X', 'Y', 'Z']

def get_result2(str, score):
    #rock from opponent
    if(str[0] == list1[0] and str[2] == list2[0]):
        score += 3
    elif(str[0] == list1[0] and str[2] == list2[1]):
        score += 1
    elif(str[0] == list1[0] and str[2] == list2[2]):
        score += 2

# paper from opponent
    elif(str[0] == list1[1] and str[2] == list2[0]):
        score += 1
    elif(str[0] == list1[1] and str[2] == list2[1]):
        score += 2
    elif(str[0] == list1[1] and str[2] == list2[2]):
        score += 3

#scissors from opponent
    elif(str[0] == list1[2] and str[2] == list2[0]):
        score += 2
    elif(str[0] == list1[2] and str[2] == list2[1]):
        score += 3
    elif(str[0] == list1[2] and str[2] == list2[2]):
        score += 1

    return score

def get_result(str, score):
    #rock from opponent
    if(str[0] == list1[0] and str[2] == list2[0]):
        score += 3
    elif(str[0] == list1[0] and str[2] == list2[1]):
        score += 6
    elif(str[0] == list1[0] and str[2] == list2[2]):
        score += 0

# paper from opponent
    elif(str[0] == list1[1] and str[2] == list2[0]):
        score += 0
    elif(str[0] == list1[1] and str[2] == list2[1]):
        score += 3
    elif(str[0] == list1[1] and str[2] == list2[2]):
        score += 6

#scissors from opponent
    elif(str[0] == list1[2] and str[2] == list2[0]):
        score += 6
    elif(str[0] == list1[2] and str[2] == list2[1]):
        score += 0
    elif(str[0] == list1[2] and str[2] == list2[2]):
        score += 3

    return score

def get_score(str):
    score = 0
    if(str[2] ==  list2[0]):
        score += 1
    elif(str[2] == list2[1]):
        score += 2
    elif(str[2] == list2[2]):
        score += 3
    score = get_result(str, score)  

    return score 

def get_score2(str):
    score = 0
    if(str[2] ==  list2[0]):
        score += 0
    elif(str[2] == list2[1]):
        score += 3
    elif(str[2] == list2[2]):
        score += 6
    score = get_result2(str, score)  

    return score 

with open(filename, 'r') as file:
    lines = file.read().splitlines()
    # result = [x for x in lines if x[0] in list1]
    # updated_result = [re.sub(r'[^a-zA-Z0-9 ]+', '', item) for item in result]
    total_score = 0
    for item in lines:
        total_score += get_score2(item)
    
    print(total_score)

file.close()
