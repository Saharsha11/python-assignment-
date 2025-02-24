string = input("Enter a string = ")
middle = int(len(string)/2)
if len(string) % 2 == 0:
    print("Middle character = ",string[middle-1:middle+1])
else:
    print("Middle charcter = ",string[middle])