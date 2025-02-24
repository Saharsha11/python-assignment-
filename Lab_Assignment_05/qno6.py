class Sphere:
    def getData(self):
        self.r = float(input("Enter the radius = "))
    
    def area(self):
        self.a = 4*3.14*self.r**2    

    def volume(self):
        self.v = ((4*3.14*self.r**3)/3)

    def dispData(self):
        print("Area of sphere = ",self.a)
        print("Volume of sphere = ",self.v)

s1 = Sphere()
s1.getData()
s1.area()
s1.volume()
s1.dispData()