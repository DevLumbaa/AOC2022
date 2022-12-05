from collections import Counter

filename = r'E:\AnsysDev\Z_not_work\AOC\2022\puzzle1.txt'
calores_dict = {}

with open(filename, 'r') as file:
    count = 1
    total_calories = 0
    for line in file:
        if line.strip():
            total_calories += int(line.strip())
        elif total_calories>0:
            calores_dict[count] = total_calories
            count += 1
            total_calories = 0

file.close()

print(max(calores_dict.values()))

counter = Counter(calores_dict)
descending_order = counter.most_common(3)
total = 0

for i in descending_order:
    total += i[1]

print(total)
