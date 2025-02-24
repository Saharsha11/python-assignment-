with open("qno6.txt") as f:
    noOfWord = 0
    print(f.read())
    lines = f.readline()
    while lines != "":  
        words = lines.split(" ")
        noOfWord += len(words)
        lines = f.readline()
    print(f"No of words in the file = {noOfWord}")