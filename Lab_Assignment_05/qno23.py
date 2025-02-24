class StringUtils:

    @staticmethod
    def pali(word):
        temp = word
        rev = ""
        i = len(word)
        while i > 0:
            rev += word[i-1]
            i -= 1 
        if rev == temp:
            print(f"{temp} is a palindrome")
        else:
            print(f"{temp} is not a palidrome")
    
    @staticmethod
    def upperCase(word):
        print("Upper case = ", word.upper())

    @staticmethod
    def reverse(word):
        print(f"Reverse of {word} = {word[::-1]}")

s = StringUtils()
s.pali("level")
s.upperCase("hello")
s.reverse("football")
