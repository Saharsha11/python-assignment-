class Sort:
    def __init__(self):
        self.array = []

    def getdata(self):
        val = int(input("Enter the number of integer to enter = "))
        for i in range(val):
            num = int(input("Enter the number = "))
            self.array.append(num)
    
    def sorting(self):
        self.array.sort()

    def dispData(self):
        print("Sorted array = ",self.array)
    
s = Sort()
s.getdata()
s.sorting()
s.dispData()