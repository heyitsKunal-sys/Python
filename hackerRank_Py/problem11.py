# list =[45,34,23,56,37]
# list_2=[]
# list.sort()
# list_2.append(list)
# print(list_2)

# list =[45,34,23,56,37]
# print(min(list))

nums =[45,34,23,56,37]
smallest = nums[0]
for l in nums :
    if (l < smallest):
        smallest = l
print(smallest)        

