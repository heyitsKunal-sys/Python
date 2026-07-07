# To capitalize the first character of each word while preserving consecutive spaces and 
# keeping alphanumeric rules (like 12abc staying 12abc), use the capitalize() method on each split component or use a 
# regular expression.Do not use Python's built-in .title() method for this specific problem, as .title() incorrectly capitalizes 
# letters after numbers 
# (e.g., changing 12abc into 12Abc)



def solve(s):
    # Split by spaces, capitalize each word, and rejoin them with a space
    return ' '.join(word.capitalize() for word in s.split(' '))

# Example Usage:
print(solve("chris alan"))   # Output: Chris Alan
print(solve("12abc"))        # Output: 12abc
print(solve("alison  heck")) # Output: Alison  Heck (preserves extra spaces)
print(solve("1 w r 2"))  ##1 W R 2


# s.split(' '): Splitting explicitly on a single space ' ' ensures that empty strings caused by consecutive extra spaces are preserved.


# word.capitalize(): This method only converts the very first character of the string to uppercase if it is a letter. 
# If it begins with a number (like 12abc), it leaves it exactly as it is.