file = open('Day1/numbers.txt' , 'r')
numbers = file.read()
list1 = []
list2 = []
newlist = numbers.split('\n')
splitlist = [item.split() for item in newlist]
for i,n in enumerate(splitlist):
    list1.append(splitlist[i][0])
    list2.append(splitlist[i][1])

finalcount = 0

list1.sort()
list2.sort()

intlist1 = [int(x) for x in list1] 
intlist2 = [int(x) for x in list2]

for i in range(len(intlist1)):
    temp = intlist2[i] - intlist1[i]
    finalcount = finalcount + abs(temp)
    print(finalcount)

print(finalcount)
