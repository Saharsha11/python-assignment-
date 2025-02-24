class Battery:
     
    def __init__(self,capacity):
        self.capacity = capacity

class ElectricCar:

    def __init__(self,make,model,other_battery):
        self.make = make 
        self.model = model 
        self.other_battery = other_battery

    def display(self):
        print(self.make , self.model , self.other_battery.capacity)
    
b = Battery(1400)
e = ElectricCar("Ram","BYD",b)
e.display()