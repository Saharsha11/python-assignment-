list1 = [11,22,13,74,5]
list2 = [15,1,7,8,4]

list1.sort()
list2.sort()

i = 0
j = 0 

while i < len(list1) and j < len(list2):
    if list1[i] == list2[j]:
        print("Duplicate found")
        break
    elif list1[i] > list2[j]:
        j += 1
    else:
        i += 1
    
else:
    print ("Duplicate not found")