# number = int(input("Enter the number: "))
# temp=number
# sum=0
# while number > 0:
#     r = number % 10  
#     sum =sum+(r*r*r)   
#     number = number // 10 

# if sum == temp:
#     print("Armstrong")
# else:
#     print("Not a Armstrong")   

def Armstrong(number):
    temp=number
    sum=0
    while number > 0:
        r = number % 10  
        sum =sum+(r*r*r)   
        number = number // 10 

    if sum == temp:
        print("Armstrong")
    else:
        print("Not a Armstrong") 

number = int(input("Enter the number: ")) 
Armstrong(number)  