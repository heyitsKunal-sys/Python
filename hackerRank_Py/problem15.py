# Input Format

# The first line contains a string, .
# The next line contains an integer , the index location and a string , separated by a space.

# Sample Input

# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'
# Sample Output

# abrackdabra







def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string
   
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)





#     How would you approach this?

# One solution is to convert the string to a list and then change the value.
# Example

# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
# abrackdabra
# Another approach is to slice the string and join it back.
# Example

# >>> string = string[:5] + "k" + string[6:]
# >>> print string
# abrackdabra