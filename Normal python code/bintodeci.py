# number=int(input("Enter the no:"))
# dec=0;rem=0;b=1
# while number>0:
#     rem=number%10
#     number=number//10
#     dec=dec+(rem*b)
#     b=b*2
# print("the decimal number is:",dec)

def bintodeci(number):
    dec=0;rem=0;b=1
    while number>0:
        rem=number%10
        number=number//10
        dec=dec+(rem*b)
        b=b*2
    return dec

number=int(input("Enter the no:"))
print("Decimal number is:",bintodeci(number))