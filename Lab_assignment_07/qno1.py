list1 = ["Saharsha","Ramesh","sabina"]
with open("qno1.txt","w") as f :
    for x in list1:
        f.write(f"{x}\n")
