a = int(input("enter a number:"))
b = int(input("enter second number:"))
if (b==0):
    raise ZeroDivisionError('hey our programm is not meant to divide by zero')

else:
    print(f"the division a/b is {a/b}")
# error ayega lekin humne error ko custom kiya apne hissab se
# raise ZeroDivisionError('hey our programm is not meant to divide by zero')"error"



print(f"The division a/b is {a/b}")
#  agar hum a =3 and b= 0 le to error ayega division nahi hoga