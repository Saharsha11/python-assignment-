class Stats:

    def calculate(self,add = None,avg = None):
        if add is not None and avg is not None:
            s = sum(add)
            avergae = sum(avg)//len(avg)
            return f"Sum = {s} \nAverage = {avergae}"
            
        else:
            if add is not None:
                s = sum(add)
                return f"Sum = {s}"
            else:
                avergae = sum(avg)//len(avg)
                return f"Average = {avergae}"


c = Stats()
a = c.calculate(avg=[1,4,5,2],add = [1,5,8])
print(a)