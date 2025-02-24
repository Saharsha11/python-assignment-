class Time: 
    def __init__(self,hr = 0,min = 0):
        self.hr = hr
        self.min =min
    
    def __add__(self,other):
        total_minutes = self.min + other.min
        total_hours = self.hr + other.hr + (total_minutes // 60)
        total_minutes %= 60
        return Time(total_hours, total_minutes)
    
    def display(self):
        print(f"{self.hr} hr {self.min} min")
    
t1 = Time(2, 50)
t2 = Time(1, 30)

# Creating a third non-initialized (default initialized) time object t3
t3 = Time()

# Performing t3 = t1 + t2 using operator overloading
t3 = t1 + t2

# Display results
print("Time 1: ", end="")
t1.display()
print("Time 2: ", end="")
t2.display()
print("Sum of Time 1 and Time 2: ", end="")
t3.display()