class Square:
    def area(self,length):
        return float(length**2)

    def perimeter(self,length):
        return float(4*length)
    
class Rectangle(Square):

    def area(self, length,breadth):
        return float(length *breadth)
    
    def perimeter(self, length,breadth):
        return float(2+(length+breadth))

r = Rectangle()
print("Area = ",r.area(45,22))
print("Perimeter = ",r.perimeter(12,20))