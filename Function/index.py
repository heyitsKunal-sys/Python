def function(a , b, c):
    print( a + b + c    )

function( 12, 45, 56 )
# output113
def function2( a, b,c):
    print( a * b * c )
function2( 12, 45, 56 )

# 30240
# def average():
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     c = int(input("Enter the third number: "))
#     avg = (a + b + c) / 3
#     print("The average is: ", avg)

# average()

def squareroot ( a, b, c):
    print( a ** 0.5, b ** 0.5, c ** 0.5     
    )
squareroot( 12, 45, 56 )

# function with arguments and return type
def average(a, b, c):
    avg = (a + b + c) / 3
    return avg
result = average( 12, 45, 56 )
print("The average is: ", result)
# output 37.666666666666664

def greet(name):
    return " hello" + name

print(greet(" John"))
# output hello John
#  recursion function means a function that calls itself until it reaches a base case. It is often used to solve problems that can be broken down into smaller, similar subproblems. Here is an example of a recursive function to calculate the factorial of a number:
def factorial(n):
    if n == 0 or n==1:    
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
# output 120
# DEFAULT PARAMETER VALUE 
def greet (name , ending = "thanks"):
    print( f" hello {name} " )
    print ( ending)


greet(" John")
greet(" Jane", "goodbye")


# Ques 1 : to find greatest among 3 numbers
def greatestNumber(a,b,c):
    if ( a> b and  a> c):
        print (a)
    elif ( b>a and b> c):
        print (b)

    else:
        print(c)

greatestNumber( 3, 6 ,7)    

# Ques 2:    pRogram to convert celsius into Farenhite
def celsiusToFahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = 25
fahrenheit = celsiusToFahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Ques 3:how do you prevent a python print() function to print a new line at the end.
# we can prevent the print() function from printing a new line at the end by using the end parameter. By default, the end parameter is set to "\n", which means that a new line will be printed after each call to print(). However, we can change this behavior by setting the end parameter to an empty string or any other string we want. For example:
print("Hello", end="")
print("World")

# Ques 4 : write a recursive function to calculate the sum of first n natural numbers
def sumofNaturalnUMBERS(n):
    if n==1:
        return 1

    else:
        return n + sumofNaturalnUMBERS(n-1)
n = 5
result = sumofNaturalnUMBERS(n)
print(f"The sum of the first {n} natural numbers is: {result}")

# Ques 5: write a fucntion for multiplication table of a given number
def tabel(n):
    for i in range( 1,11):
        print ( f" {n} x {i} = {n*i}" )
number = 5
tabel(number)

# Ques 6: fabonacci series
def function (n):
    a = 0
    b= 1
    c = 0
    for i in range(n):

        print(c, end=" ")
        a = b
        b = c
        c = a + b
n = 10
function(n)

# Ques 7 : Write a python function to remove a given word from a list and strip it at the same time
def remove_word():
    word_list = ["apple", "banana", "cherry", "date", "fig", "grape"]
    word_to_remove = input("Enter the word to remove: ")
    if word_to_remove in word_list:
        word_list.remove(word_to_remove)
        print(f"{word_to_remove} has been removed from the list.")
    else:
        print(f"{word_to_remove} is not in the list.")
    print("Updated list:", word_list)
remove_word()

        