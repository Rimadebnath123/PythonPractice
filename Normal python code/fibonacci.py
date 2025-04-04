# number = int(input("Enter the number: "))
# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(1,number+1):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print(n3, end=" ")

def fibonacci(number):
    n1=0
    n2=1
    print(n1, n2, end=" ") 
    for i in range(1,number+1):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3, end=" ")

number = int(input("Enter the number: "))
fibonacci(number)