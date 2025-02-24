circle = ("circle",15)
rectangle = ("Rectangle",10,5)
shape = input("Enter the name of the shape = ")
match shape:
    case "circle":
        print("Name = ",circle[0])
        print("Radius = ",circle[1])
    case "rectangle":
        print("Name = ",rectangle[0])
        print("Length = ",rectangle[1]) 
        print("Width = ",rectangle[2])
    case _:
        print("Invalid input")
