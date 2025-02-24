class Shape:
    def area(self):
        return 0
    
class Circle(Shape):

    def area(self,radius,side):
       return radius,side
    
c = Circle()
r,s = c.area(14,5)
print(f"Radius = {r} and side = {s}")

