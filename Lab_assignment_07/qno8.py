with open("qno6.txt") as f:
    lines = f.readlines()
    revLine = lines[::-1]
    for i in revLine:
        print(i)