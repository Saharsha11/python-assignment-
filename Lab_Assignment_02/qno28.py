list1 = [1,22,13,4,15]
list2 = [15,1,7,8,4]

common = []

list1.sort()
list2.sort()

i = 0
j = 0 

while i < len(list1) and j < len(list2):
    if list1[i] == list2[j]:
        common.append(list1[i])
        i += 1
        j += 1
    elif list1[i] > list2[j]:
        j += 1
    else:
        i += 1
    
else:
    print ("Common elements = ")
    for i in common:
        print(i)
