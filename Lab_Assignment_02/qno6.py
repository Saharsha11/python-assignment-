day = input("Enter the day = ")
match day:
    case "Sunday":
        print("Weekday")
    case "Monday":
        print("Weekday")
    case "Tuesday":
        print("Weekday")
    case "Wednesday":
        print("Weekday")
    case "Thursday":
        print("Weekday")
    case "Friday":
        print("Weekday")
    case "Saturday":
        print("Weekend")
    case _:
        print("Wrong input")