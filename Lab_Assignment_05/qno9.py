class Box:
    def __init__(self,w,h,b):
        self.w = float(w)
        self.h = float(h)
        self.b = float(b)
       
    def area(self):
        area = (2*self.w*self.h)+(2*self.b*self.h)+(2*self.w*self.b)
        return area 
    
    def volume(self):
        volume = self.w*self.h*self.b
        return volume
    
box1 = Box(14,22,17)
a = box1.area()
v = box1.volume()
print("Area of the box = ",a)
print("Volume of the box = ",v)