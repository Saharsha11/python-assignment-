def outer(num):
    
    def inner(num):
        print(num)
    inner(num)
outer(11)