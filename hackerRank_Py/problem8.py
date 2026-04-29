# Sample Input 0

# 1
# 1
# 1
# 2
# Sample Output 0

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]



x = int(input("enter a number :"))
y = int(input("enter a number :"))
z = int(input("enter a number :"))
n = int(input("enter a number :"))
result= []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                result.append([i,j,k])
print(result)                

# logic: lets say x = 1, y=1 , z=1
#  range(x+1):0,1
#  range(y+1):0,1
#  range(z+1):0,1

# how loop will run
# i = 0:
#     j=0:
#       k = 0 - [0,0,0]
#       k=1 - [0,0,1]
#     j=1:
#       k=0 - [0,1,0]
#       k=1 - [0,1,1]  

# i= 1:
#     j=0:
#       k=0 - [1,0,0]
#       k=1 =[1,0,1]
#     j=1 :
#       k=0 -[1,1,0]
#       k=1 -[1,1,1]



