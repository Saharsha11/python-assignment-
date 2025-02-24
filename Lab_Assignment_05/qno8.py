class Calculator:
    def __init__(self,a,b):
        self.a = a 
        self.b = b 
    
    def addition(self):
        print(f"Addition = {self.a+self.b}")

    def substraction(self):
        print(f"Substraction = {self.a-self.b}")

    def multiplication(self):
        print(f"multiplication = {self.a*self.b}")

    def division(self):
        print(f"Division = {self.a/self.b}")
   
c1 = Calculator(48,8)
c1.addition()
c1.substraction()
c1.multiplication()
c1.division()