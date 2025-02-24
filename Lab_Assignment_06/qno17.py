class Publication:

    def getData(self,title,price):
        self.title = title
        self.price = price
    
class Book(Publication):

    def getData(self,title,price,pages):
        super().getData(title,price)
        self.pages = pages
    
    def putdata(self):
        print(f"Title = {self.title}")
        print(f"Price = {self.price}")
        print(f"Pages = {self.pages}")

class CD_ROM(Publication):

    def getData(self,title,price,playtime):
        super().getData(title,price)
        self.playtime = playtime
    
    def putdata(self):
        print(f"Title = {self.title}")
        print(f"Price = {self.price}")
        print(f"Playtime = {self.playtime}")

b = Book()
b.getData("Hobbit",350,200)
b.putdata()
c = CD_ROM()
c.getData("Jungle Book",400,"1hr 20min")
c.putdata()
        