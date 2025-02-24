def outer():
    s = "This is outer function"
    
    def inner():
        s = "This is the inner fucntion"
        print(s)
    inner()
    print(s)
outer()