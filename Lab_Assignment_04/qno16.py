def make_multiplier(n):

    def multiply(n):
        return (n*n)

    return multiply(n)

print("Multiply = ",make_multiplier(10))