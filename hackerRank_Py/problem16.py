# Sample Input

# ABCDCDC
# CDC
# Sample Output

# 2





string = "ABCDCD"
sub_string = "CD"
count = 0
for i in range (len(string)):
    if string[i:i + len(sub_string)] == sub_string:           #slicing
        count = count+1
        print(count)

