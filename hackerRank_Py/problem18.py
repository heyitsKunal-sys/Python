# using list comprehenison
nums =[1,2,3,4,5]
double_numbers = [x*2 for x in nums]
print(double_numbers)

# using for loop
nums1 = [1,2,3,4,5]
for i in nums1:
    print(i *2)

# using map
nums3= [1,2,3,4,5]
def double(x):
    return x*2

result = list(map(double , nums3))
print(result)

