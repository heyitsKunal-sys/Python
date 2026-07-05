# Input Format

# A single line containing a string S 

# Output Format

# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.


# Sample Input

# qA2
# Sample Output

# True
# True
# True
# True
# True

if __name__ == '__main__':
    s = input()
    print(any(item.isalnum() for item in s))
    print(any(item.isalpha() for item in s))
    print(any(item.isdigit() for item in s))
    print(any(item.islower() for item in s))
    print(any(item.isupper() for item in s))
    # any() is a built in func which checks at least one value is true


# using if else

s = input()

# isalnum()
flag = False
for ch in s:
    if ch.isalnum():
        flag = True
        break
print(flag)

# isalpha()
flag = False
for ch in s:
    if ch.isalpha():
        flag = True
        break
print(flag)

# isdigit()
flag = False
for ch in s:
    if ch.isdigit():
        flag = True
        break
print(flag)

# islower()
flag = False
for ch in s:
    if ch.islower():
        flag = True
        break
print(flag)

# isupper()
flag = False
for ch in s:
    if ch.isupper():
        flag = True
        break
print(flag)