# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
# Sample Input 0

# 5
# 2 3 6 6 5
# Sample Output 0

# 5
n = int(input())
a = list(map(int,input().split()))

score = sorted(list(set(a)))
print(score[-2])

# input(): Reads the entire line of text you typed as a single string (e.g., "10 20 30").
# .split(): Chops that string into a list of smaller strings based on the spaces (e.g., ["10", "20", "30"]).
# map(int, ...): This is the "converter." It takes every individual string in that list and applies the int() function to it, turning them into real integers so you can do math with them.
# list(...): The map function creates an "iterator" (a lazy object). Wrapping it in list() forces it to actually generate all those integers and store them in a standard Python list.

# set(a): A set cannot have duplicate items. By passing your list a into set(), Python instantly deletes any repeating numbers.
# Example: [10, 5, 10, 8] becomes {5, 8, 10}.
# list(...): This converts the set back into a list format so you can manipulate it more easily.
# sorted(...): This takes that list and puts the numbers in order from smallest to largest.
# n= 5
# list = [2,4,3,5,7]
# score = sorted(list)
# print(score[-2])