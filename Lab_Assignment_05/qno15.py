class TicketBooth:

    def __init__(self,person,ticket):
        self.person = person
        self.ticket = ticket
        print("People visited = ",person)
        print("Ticket bought = ",ticket)

    def people(self):
        self.p = input("Do you want to buy a ticket(y/n) = ")
        ans = self.p.lower()
        self.amount = self.ticket*2.50
        if ans == 'n':
            self.person += 1
        else:
            self.person +=1
            self.ticket += 1 
            self.amount +=2.50

    def total(self):
        print("Total number of people that visited the booth = ",self.person)
        print(f"Total ticket sold = {self.ticket}")
        print(f"Total amount of money collected = {self.amount}")

    
p = TicketBooth(20,15)
p.people()
p.total()