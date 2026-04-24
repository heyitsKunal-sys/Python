def main():
    try:
        a = int(input("enter a number:"))  # 34
        print(a) 
        return
    except Exception as e:
        print(e)
        return

    finally:
        print("iam inside else") 
    # code successfully run ho ya na ho finally chal pdega.
    # finally ka use kre bina bhi sidha print kre  print("iam inside else") 
    # tab bhi chal padega
    # so finally use hota h Functions k case me. func k case me finnaly chlega chahe input hhum valid de ya nahi. nahi to 

    #  print("iam inside else")  ye statement nahi chalegi