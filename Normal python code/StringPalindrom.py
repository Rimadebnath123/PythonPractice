# def is_palindrome(s):
#     s = s.lower().replace(" ", "")  # Convert to lowercase & remove spaces
#     return s == s[::-1]  # Check if the string is the same when reversed

# string = input("Enter a string: ")

# if is_palindrome(string):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


# s = input("Enter the string: ")
# rev = s[::-1]

# if s == rev:
#     print("String is a palindrome")
# else:
#     print("Not a palindrome")

s = input("Enter the string: ")
rev = ""
#-1 → This is the stopping condition (not inclusive).This is the step value, which means the loop moves backward.
for i in range(len(s) - 1, -1, -1):
    rev += s[i]

if s == rev:
    print("String is a palindrome")
else:
    print("Not a palindrome")