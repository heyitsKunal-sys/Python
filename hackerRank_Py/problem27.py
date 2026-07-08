# Sample Input

#  1 2
#  3 4
# Sample Output

#  (1, 3) (1, 4) (2, 3) (2, 4)

# most optimized way
from itertools import product

# Read space-separated integers for list A and list B
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# Compute the Cartesian product
result = product(A, B)
# Unpack and print the tuples separated by a space
print(*result)
# logic:
# input().split(): Reads the input line as a string and splits it by spaces into individual string numbers.
# map(int, ...): Converts each of those split string elements into actual Python integers.
# product(A, B): Computes the ordered Cartesian product. Since A and B are already sorted in the input, the product will automatically be in sorted order
# .print(*result): The asterisk * operator unpacks the generator. It passes every single tuple as a separate argument to the print() function,
# which defaults to separating them with spaces and omits any outer brackets [].


















import itertools 
A = [1,2]
B= [3,4]
print(*itertools.product(A, B))


# list comprehension
A = [1, 2]
B = ['a', 'b']

# Calculate using a single-line nested loop
result = [(a, b) for a in A for b in B]
print(result)
# Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]