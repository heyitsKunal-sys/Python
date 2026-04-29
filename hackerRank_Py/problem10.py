# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

n = int(input("enter number:"))
students = []
for _ in range(n):
    name = input("enter name:")
    score = float(input("enter score:"))
    students.append([name, score])

scores = sorted(set([s[1] for s in students]))

second_lowest = scores[1]

names = [s[0] for s in students if s[1] == second_lowest]
# [name for name, score in students if score == second_lowest]

names.sort()
# ['Harry', 'Berry']
# ['Berry', 'Harry'] :sort

for name in names:
    print(name)
