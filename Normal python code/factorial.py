# number=int(input("Enter the no:"))
# fact=1
# for i in range(1,number+1):
#     fact=fact*i

# print("the factorial no is",fact)

#OR

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact    

number=int(input("Enter the no:"))
print("the factorial no is",factorial(number))
