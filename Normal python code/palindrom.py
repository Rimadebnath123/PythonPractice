# number = int(input("Enter the number: "))
# temp = number 
# sum = 0  

# while number > 0:
#     r = number % 10  
#     sum = sum * 10 + r  
#     number = number // 10 

# if sum == temp:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

#OR


#the function palindrom(number) does not return anything explicitly, meaning its return type is None.
def palindrom(number):
    temp = number 
    sum = 0  

    while number > 0:
        r = number % 10  
        sum =r+(sum * 10)   
        number = number // 10 

    if sum == temp:
        print("Palindrome")
    else:
        print("Not a Palindrome")

number = int(input("Enter the number: "))
palindrom(number)

# def palindrom(number):
#     temp = number 
#     rev = 0  

#     while number > 0:
#         r = number % 10  
#         rev = rev * 10 + r  
#         number = number // 10 

#     return rev == temp  # Returns True if palindrome, False otherwise

# number = int(input("Enter the number: "))
# if palindrom(number):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
