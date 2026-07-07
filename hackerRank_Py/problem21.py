# pattern
N, M = map(int, input().split())
pattern = '.|.'

# TOP
for i in range(1, N, 2):
    print((pattern * i).center(M, '-'))
   
# MIDDLE
print('WELCOME'.center(M, '-'))

# BOTTOM
for i in reversed(range(1, N, 2)):
    print((pattern * i).center(M, '-'))