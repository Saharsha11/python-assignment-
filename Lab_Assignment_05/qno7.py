class Greatest:
    def input(self):
        self.large = []
        self.num = int(input("Enter how many number u want to enter = "))
        for i in range(self.num):
            n = int(input("Enter the number = "))
            self.large.append(n)

    def largest(self):
        self.large.sort()
        print(self.large)

    def display(self):
        l = len(self.large)-1
        print("Largest num = ",self.large[l])
            

l = Greatest()
l.input()
l.largest()
l.display()