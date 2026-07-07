
# Sample Input

# STDIN       Function
# -----       --------
# AABCAAADA   s = 'AABCAAADA'
# 3           k = 3
# Sample Output

# AB
# CA
# AD


def merge_the_tools(string, k):
     for i in range(0, len(string), k):
        # Slice the subsegment of length k
        subsegment = string[i : i + k]
        
        # dict.fromkeys() removes duplicates while keeping the insertion order
        unique_chars = "".join(dict.fromkeys(subsegment))
        
        # Print the final result for this chunk
        print(unique_chars)
    


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# How it processes your sample input:
# If you pass the string AABCAAADA and k = 3, the script breaks it down like this:
# First chunk (i=0 to 3): 'AAB'  ->   removes duplicate 'A'   ->  Prints AB
# Second chunk (i=3 to 6): 'CAA' ->    removes duplicate 'A'   ->   Prints CA
# Third chunk (i=6 to 9): 'ADA'  ->   removes duplicate 'A'   ->  Prints AD