# number=int(input("Enter the no:"))
# bin=0;rem=0;p=1
# while number>0:
#     rem=number%2
#     number=number//2
#     bin=bin+(rem*p)
#     p=p*10
# print("Bin number is:",bin)


def decibin(number):
    bin=0;rem=0;p=1
    while number>0:
        rem=number%2
        number=number//2
        bin=bin+(rem*p)
        p=p*10
    return bin
number=int(input("Enter the no:"))
print("Bin number is:",decibin(number))