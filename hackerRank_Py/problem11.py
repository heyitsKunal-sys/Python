# list =[45,34,23,56,37]
# list_2=[]
# list.sort()
# list_2.append(list)
# print(list_2)

# list =[45,34,23,56,37]
# print(min(list))

list =[45,34,23,56,37]
smallest = list[0]
for l in list :
    if (l < smallest):
        smallest = l
print(smallest)        

