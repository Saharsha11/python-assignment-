class Book:

    def __init__(self,book_id,pages):
        self.book_id = book_id
        self.pages = pages 
    
class FictionalBooks(Book):

    def __init__(self, book_id, pages,name):
        super().__init__(book_id, pages)
        self.name = name 
        
    def display(self):
        print(f"name = {self.name}")
        print(f"Book id = {self.book_id}")
        print(f"Pages = {self.pages}")

f = FictionalBooks(1985,205,"Hobbit")
f.display()
