value = input("Enter a character = ")
if value.isalpha():
    print(f"{value} is a alphabet.")
elif value.isdigit():
    print(f"{value} is a digit.")
else:
    print(f"{value} is a special character.")
