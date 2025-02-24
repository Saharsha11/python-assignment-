class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model 

class Car(Vehicle):
    def __init__(self, make, model,year):
        super().__init__(make, model)
        self.year = year 

ferrai = Car("Hitler","Spida",2000)

print(ferrai.make,ferrai.model,ferrai.year)

        