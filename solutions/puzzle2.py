import re

filename = r'E:\AnsysDev\Z_not_work\AOC\2022\puzzle2.txt'
#A=X=ROCK
#B=Y=PAPER
#C=Z=SCISSORS

list1 = ['A', 'B', 'C']
list2 = ['X', 'Y', 'Z']

def get_result(str, score):
    #rock from opponent
    if(str[0] == list1[0] and str[1] == list2[0]):
        score += 3
    elif(str[0] == list1[0] and str[1] == list2[1]):
        score += 6
    elif(str[0] == list1[0] and str[1] == list2[2]):
        score += 0

# paper from opponent
    elif(str[0] == list1[1] and str[1] == list2[0]):
        score += 0
    elif(str[0] == list1[1] and str[1] == list2[1]):
        score += 3
    elif(str[0] == list1[1] and str[1] == list2[2]):
        score += 6

#scissors from opponent
    elif(str[0] == list1[2] and str[1] == list2[0]):
        score += 6
    elif(str[0] == list1[2] and str[1] == list2[1]):
        score += 0
    elif(str[0] == list1[2] and str[1] == list2[2]):
        score += 3

def get_score(str):
    score = 0
    if(str[1] ==  list2[0]):
        score += 1
    elif(str[1] == list2[1]):
        score += 2
    elif(str[1] == list2[2]):
        score += 3
    get_result(str, score)  
    return score 

with open(filename, 'r') as file:
    lines = file.read().splitlines()
    result = [x for x in lines if x[0] in list1]
    updated_result = [re.sub(r'[^a-zA-Z0-9 ]+', '', item) for item in result]
    total_score = 0
    for item in updated_result:
        total_score += get_score(item)
    
    print(total_score)

file.close()
