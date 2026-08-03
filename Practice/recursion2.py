def print_numbers(n):
    for i in range(1, n ):
        print(i)

print_numbers(10)

def fun(n):
    i = 1
    while (i<=n):
        print (i)
        i+=1

fun(5)

# using recursion: print 1 to N

def newFun(i,n):
    if i > n:
        return
    print(i)
    newFun(i+1 , n)
newFun(1,5)    
#1 2 3 4 5


# print hello n times
def new(n):
    if n==0:
        return
    print("hello")
    new(n-1)
new(5)      

# PRINT N to 1 :
def nToOne(n):
    if n==0:
        return
    print(n)
    nToOne(n-1)
nToOne(5)    

# sum of first N natural numbers: functional recursion
def sumOfNaturalNumbers(n):
    if n==0:
        return 0
    return n + sumOfNaturalNumbers(n-1)
print(sumOfNaturalNumbers(5))

# same ques in Parametrized recursion:
def sum_n(n, ans):
    if n == 0:
        print(ans)
        return

    sum_n(n - 1, ans + n)

sum_n(5, 0)

# Factorial of N:
def factorial (n):
    if n==0:
        return 1
    return n* factorial(n-1)

print(factorial(5))

def factorial2 (n, result):
    if n== 0:
        return 1
    factorial2(n-1 , result * n)

factorial2(5, 1)


# fibonacci series
def fibonacci(n):
    a =0
    b=1
    for i in range(n):
        print (a)
        next = a+b
        a= b
        b = next

fibonacci(10)    

# fibonacci using Recursion  
def fibonacci2(n):
    if n <= 1:
        return n

    return fibonacci2(n - 1) + fibonacci2(n - 2)

for i in range(8):
    print(fibonacci2(i), end=" ")