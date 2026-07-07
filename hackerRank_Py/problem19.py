n = int(input())

for i in range(n):
    print(" "*(n-1-i) + (2*i+1) * "H")

for i in range(n+1):
    print(" " * ((n-1)//2) + "H" * n + " " * (3*n) + "H" * n)

for i in range((n+1)//2):
    print(" " * ((n-1)//2) + "H" * (n*5))

for i in range(n+1):
    print(" " * ((n-1)//2) + "H" * n + " " * (3*n) + "H" * n)

for i in range(n):
    print(" " * (3*n + (i+n)) + (2*(n-1-i)+1) * "H")