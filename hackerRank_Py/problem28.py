import itertools

# Read input and split it into the string and the size
user_input = input().split()

# Extract the string and convert the size to an integer
input_string = user_input[0]
size = int(user_input[1])

# Generate all permutations of the given size
permutations = itertools.permutations(input_string, size)

# Convert each tuple into a string and sort them lexicographically
sorted_permutations = sorted("".join(p) for p in permutations)

# Print each permutation on a new line
for perm in sorted_permutations:
    print(perm)



# logic:
# 1. Reading and Splitting the Inputpythonuser_input = input().split()
# Use code with caution.input(): Reads the entire line typed by the user as a single string: "HACK 2"..split(): Splits that string wherever there is a space.Result: user_input becomes a list of strings: ['HACK', '2'].
# 2. Extracting the Variablespythoninput_string = user_input[0]
# size = int(user_input[1])
# Use code with caution.user_input[0]: Grabs the first item from the list, which is "HACK".user_input[1]: Grabs the second item, which is the string "2".int(...): Converts the string "2" into the actual integer 2 so Python can use it as a counter.
# 3. Generating the Permutationspythonperms = itertools.permutations(input_string, size)
# Use code with caution.This is the core engine. itertools.permutations("HACK", 2) finds every possible pair of letters where the order matters (meaning "HA" and "AH" are treated as two different results).Result: It creates an internal Python generator containing tuples like ('H', 'A'), ('H', 'C'), ('A', 'H'), and so on.
# 4. Joining and Sorting (The List Comprehension)pythonsorted_perms = sorted(["".join(p) for p in perms])
# Use code with caution.This line actually does two things at once:["".join(p) for p in perms]: Loops through the tuples and combines them. For example, the tuple ('H', 'A') becomes the unified string "HA".sorted(...): Takes that fresh list of strings and rearranges them into strict alphabetical (lexicographical) order.Result: sorted_perms becomes ['AC', 'AH', 'AK', 'CA', ... , 'KH'].
# 5. Printing the Final Outputpythonfor p in sorted_perms:
#     print(p)
# Use code with caution.This loop visits every single string inside our sorted list one by one and prints it. Because print() automatically starts a new line after every execution, your output stacks vertically exactly like the sample format