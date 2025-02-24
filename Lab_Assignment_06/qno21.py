from abc import ABC,abstractmethod
class Lecturer(ABC):

    @abstractmethod
    def getdata(self):
        pass

    @abstractmethod
    def putdata(self):
        pass

class Part_time(Lecturer):

    def getdata(self,payPerHour):
        self.payPerHour  = payPerHour

    def putdata(self):
        print(f"Pay per hour = {self.payPerHour}")


class Fulltime(Lecturer):
    def getdata(self,payPerMonth):
        self.payPerMonth = payPerMonth

    def putdata(self):
        print(f"Pay per month = {self.payPerMonth}")
    

p = Part_time()
p.getdata(8)
p.putdata()
f = Fulltime()
f.getdata(40000)
f.putdata()

        

