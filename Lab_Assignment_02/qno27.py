def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for uniformity
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # If lengths of strings are not equal, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Convert strings to sorted lists
    list1 = sorted(str1)
    list2 = sorted(str2)

    # Initialize index for the while loop
    i = 0

    # Compare each character using a while loop
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1

    return True

# Input strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if they are anagrams
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

