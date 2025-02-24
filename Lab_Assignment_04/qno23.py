def power(b,e):
    if e == 0:
        return 1
    else:
        return b * power(b,e-1)
    
print("Power = ",power(2,5))