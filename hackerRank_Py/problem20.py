# Sample Input :

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output :

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap

def wrap(string, max_width):
    return (textwrap.fill(string , max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# using loops

text = "ABCDEFGHIJKLMNOP"
width = 4
for i in range(0, len(text),width):
    print(text[i:i+width])

# here we use 3 aruguments in range(start,stop,step)
# start =0 , step= width 
# 1st iteration range 0 to 4
# print(text[i:0+4]): 0:4 ABCD now i becomes 4
# 2nd iteration: i=4 slice text[4:8] and goes on..