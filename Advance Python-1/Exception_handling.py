try:
    a = int(input("hey,enter a number: "))
    print(a)
# #agr hum try except ka use na kre to ValueError ata h
# lekin inke use se programm crash  hua 
# hey,enter a number: kunal
# invalid literal for int() with base 10: 'kunal' ye output ayii

# hum ek specific error ko bhi handel kr skte ha
except ValueError as v:
    print("heyyyy")
    print(v)
#hey,enter a number: harry
# heyyyy : humara heyy print ho gya . mtlv kisi bhi error ane pe hum koi bhi message dikha skte ha.
# invalid literal for int() with base 10: 'harry'
except Exception as e:
    print(e)    
    

