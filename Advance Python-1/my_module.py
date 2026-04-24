def myFunc():
    print("hey man")

# myFunc()
# print(__name__)
# output: hey man
# __main__

if __name__ == "__main__": 
    # if this code is executed by running the file
    # its present in
    print("we are directly running this code")
    myFunc()
    print(__name__) 

    # scn kya h __name__ evaluate krta  name
    #  ab dusri file me 
    # from my_module import myFunc
    # ye run nahi kyuki file ka name me main h jbki hina module chahiye the
    # jis file ko import krna h us file ka name hona chahiye