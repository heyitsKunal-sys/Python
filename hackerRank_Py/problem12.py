# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

# Sample Input 0

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output 0

# 56.00
# n = int(input("enter a number:"))
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()     ## (*)with a variable name line refers to extended iterable package. if we dont use it it will gibe 
#     ["kunal" ,"67","68,"69"]          ##   give error like more than 2 values are not inserted.
#     scores = list(map(float, line))    ## this convert string to list [67.0,68.0,69.0]
#     student_marks[name] = scores
    #    {
    #     "kunal" :[67.0,68.0,69.0]
    #     "kunal2":
    #     "kunal3":
    #    }
# query_name = input()   ##input(kunal)
# marks = student_marks[query_name]           #marks = student_marks[kunal] ## [67.0,68.0,69.0]
# avg = sum(marks) / len(marks)
   #[67.0,68.0,69.0]/3
# print(f"{avg:.2f}")


n = int(input())
data = {}

for i in range(n):
    arr = input().split()

    name = arr[0]
    marks = list(map(float, arr[1:]))

    data[name] = marks

search_name = input()

marks = data[search_name]
average = sum(marks) / len(marks)

print(f"{average:.2f}")