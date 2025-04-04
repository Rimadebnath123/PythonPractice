number=int(input("Enter the no:"))
oct=0;rem=0;b=1
while number>0:
    rem=number%8
    number=number//8
    oct=oct+(rem*b)
    b=b*10
print("the octal number is:",oct)

# def decitocot(number):
#     oct=0;rem=0;b=1
#     while number>0:
#         rem=number%8
#         number=number//8
#         oct=oct+(rem*b)
#         b=b*10
#     return oct

# number=int(input("Enter the no:"))
# print("Octal number is:",decitocot(number))

#122