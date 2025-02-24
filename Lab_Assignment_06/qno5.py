class Rectangle:

    def __init__(self,height,width):
        self.height = height
        self.width = width

        if self.height < 0 or self.width < 0 :
            print("Height and width must be positive number")
            exit(1)
    
    def calcArea(self):
        print(f"Area = {self.height * self.width}")

r = Rectangle(15, 6)
r.calcArea()

