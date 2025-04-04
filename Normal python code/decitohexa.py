# conversion_table=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
# number=int(input("Enter the no:"))
# hexa='';rem=0;b=1
# while number>0:
#     rem=number%16
#     hexa=conversion_table[rem]+hexa
#     number=number//16
   
# print("the hexa number is:",hexa)
#205

number = int(input("Enter the number: "))  
print("Hexadecimal:", hex(number)[2:].upper())  
