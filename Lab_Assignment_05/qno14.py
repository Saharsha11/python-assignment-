class Booth:
    def people(self):
        self.p = int(input("Enter the people that bought the ticket ="))
    
    def total(self):
        print("Total number of people that visited the booth = ",self.p)
        print(f"Total amount of money collected = {self.p*2.50}")
    
p = Booth()
p.people()
p.total()