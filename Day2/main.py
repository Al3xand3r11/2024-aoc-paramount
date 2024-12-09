def has_duplicates(lst):
    return len(lst) != len(set(lst))

descendingLevels = 0
ascendingLevels = 0
levels = 0
isSafe = True
myList = []
origin = 0
with open('Day2/input.txt' , 'r') as file:
    for line in file:
        line = line.split()
        if line:
            line = [int(i) for i in line]
            myList.append(line)
        
for row in myList:
    if row == sorted(row):
        if has_duplicates(row):
            pass
        else:
            ascendingLevels += 1
            print(row)

for row in myList:
    if row == sorted(row, reverse=True):
        if has_duplicates(row):
            pass
        else:
            descendingLevels += 1

print(ascendingLevels)
print(descendingLevels)
    


