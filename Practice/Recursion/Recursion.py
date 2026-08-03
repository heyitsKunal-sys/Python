def hello(n):
    if n==0:
        return

    print("Hello")
    hello(n-1)

hello(5)    


def fun(n):
    if n==0:
        return

    print(n)
    fun(n-1)

fun(3)