# number=int(input("Enter the no:"))
# count=0
# for i in range(1,number+1):
#     if number % i == 0 :
#         count+=1

# if count==2:
#     print("this is a prime number")
# else:
#     print("this is not a prime number")

#OR

# def prime(n):
#     count=0
#     for i in range(1,n+1):
#         if n % i == 0 :
#             count+=1    

#     if count==2:
#         print("this is a prime number")
#     else:
#         print("this is not a prime number")

# number=int(input("Enter the no:"))
# prime(number)

#OR

def prime(n):
    count=0
    for i in range(1,n+1):
        if n % i == 0 :
            count+=1    
    return count

number=int(input("Enter the no:"))
count = prime(number) 

if count==2:
    print("this is a prime number")
else:
    print("this is not a prime number")