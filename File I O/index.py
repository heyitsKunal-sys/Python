f = open("File I O/file.txt", "r")
data = f.read()
print(data)
f.close()

# We can also use f.readline() function to read one full line at a time. 
# # f.readline() # Read one line from the file. 
# We can also use f.readlines() function to read all the lines in a file and return them as a list.
f = open("File I O/file.txt", "r")
data = f.readlines()    
print(data)
f.close()
# output = ['hey kunal this side']

# MODES OF OPENING A FILE 
# r – open for reading 
# w - open for writing  
# a - open for appending 
# +  - open for updating. 
# ‘rb’ will open for read in binary mode. 
# ‘rt’ will open for read in text mode. 

r = open("File I O/file.txt" , "r")
print(r.read())
r.close()

w = open("File I O/file.txt" , "w")
w.write("This is a new line." )
w.close()

a = open("File I O/file.txt", "a")
a.write("\nThis line is appended.")
a.close()

r_plus = open("File I O/file.txt", "r+")
print(r_plus.read())
r_plus.write("\nThis line is added using r+ mode.")
r_plus.close()

# The best way to open and close the file automatically is the with statement. 
with open("File I O/file.txt", "r") as f:
    data = f.read()
    print(data)


# Ques 1 : To read the text and find out the letter Bird from poem.txt file.
f =open("File I O/poem.txt", "r")
data = f.read()
if "Bird" in data:
    print("yes")
    
else:
    print("no")
f.close()

# Ques 2: The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# # score whenever the game() function breaks the Hi-score.  

import random 
def game():
    print("Playing the game...")
    score = random.randint(0, 100)
    print ("Your score is:", score)
    if (int (score) > int(high_score)):
        with open("File I O/hiscore.txt", "w") as f:
            f.write(str(score))
        print("Congratulations! You have the new Hi-score."
        )
    else:
        print("Sorry, you did not beat the Hi-score. Try again!")
with open("File I O/hiscore.txt", "r") as f:
    high_score = f.read()
    if high_score == "":
        high_score = 0
print("Current Hi-score is:", high_score)
game()
    
# Ques 3 : Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old. 

def multiplication_table(n):
    for i in range (1,11):
        result = n * i
        with open(f"File I O/Table/Table.txt_{n}.txt", "w") as f:
            f.write(f"{n} x {i} = {result}\n")

    
for i in range ( 2,22):
    multiplication_table(i)



def multiplication_table(n):
    for i in range( 1,11):
        print (f"{n} x {i} = {n*i}")

for i in range ( 1,3):
    multiplication_table(i)

# Ques 4 : A file contains  a word multiple times. Write a program to read the file and replace the word is present in the file with another word and write the new content to a new file.




# with open("File I O/poem.txt", "r") as f:
#     data = f.read()
# with open("File I O/poem.txt", "w") as f:
#     new_word = input("Enter the word to be replaced: ")
#     replacement_word = input("Enter the replacement word: ")
#     new_data = data.replace(new_word, replacement_word)
#     f.write(new_data)
 

# Ques 5 : Write a program to find out whether a file is identical & matches the content of 
#  another file.

def identical_files():
    with open("File I O/file.txt", "r") as f1:
        content1 = f1.read()
    with open("File I O/poem.txt", "r") as f2:
        content2 = f2.read()
        if content1 == content2:
            print("The files are identical.")
        else:
            print("The files are not identical.")


            


identical_files( )


