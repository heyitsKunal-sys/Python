def is_leap(year):
    if ( year % 400== 0 ):
        return(True)
    elif ( year % 100 ==0):
        return(False)
    elif (year % 4 == 0):
        return(True)
    else:
        return (False)    
year = int(input())
print(is_leap(year))
# every 4 is a leap but every 100 is not and every 400 is leap
# eg 2000 is a leap year
#  2000 % 400 == 0 but 2100 is not a leap pr 2100 % 4 ==0 but % 100 = 0 is not a leap 