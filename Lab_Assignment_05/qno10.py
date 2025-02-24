class Intamount:

    def getData(self,p,r,t):
        self.principal = float(p)
        self.rate = float(r)
        self.time = int(t)

    def interest(self):
        self.value = self.principal * self.time *self.rate
        print("Interest = ",self.value)
    
    def amount(self):
        self.amt = self.principal*(1+self.rate*self.time)
        print("Total amount = ",self.amt)

i1 = Intamount()
i1.getData(10000,10,3)
i1.interest()
i1.amount()