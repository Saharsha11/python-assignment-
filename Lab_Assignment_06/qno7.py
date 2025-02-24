class Address:
    def __init__(self,street, city):
        self.street = street
        self.city = city 

class Person:
     
    def __init__(self,other_address):
        print(f"Street = {other_address.street} and city = {other_address.city}")
    
a = Address("chamati","kathamandu")
p = Person(a)
        