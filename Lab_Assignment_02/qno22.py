age = []
for i in range(10):
    a = int(input("Enter the age of people = "))
    age.append(a)
count = 0
for x in range(10):
    if age[x]>25 and age[x]<50:
        count += 1
print("Number of people of age group 25 to 50 = ",count)