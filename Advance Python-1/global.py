a = 89

def fun():
    global a   #global upar wale a ko change kr raha h to vo 3 ban gya or global nahi likhe to 89 or 3 print honge
    a= 3
    print(a)

fun()
print(a)