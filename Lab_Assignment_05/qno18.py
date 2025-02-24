class Counter:
    count = 0
    
    def __init__(self):
        Counter.count +=1

    @staticmethod
    def get_total_count():
        print("Total counter = ",Counter.count)
    
c1 = Counter()
c2 = Counter()
Counter.get_total_count()