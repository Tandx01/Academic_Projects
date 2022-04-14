"""
Name: Taha Andac
ID : 75785
Section : 03"""

# Checks validity of a given date.
# Prints valid date or invalid date.

day= int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

max_day = 31
max_month = 12
#is_valid checks the validity of given date.
is_valid = 0
#is_leap checks leap years.
is_leap = 0

if 0 < day <= max_day:
   is_valid +=1
   
else:
    print("Invalid day")

    
if 0 < month <= max_month:
    is_valid +=1
    
else:
    print("Invalid month")

    
if 0 < year :
    is_valid +=1

else:
    print("Invalid year")
    

if is_valid == 3:
                
    if month == 2:
        if year % 4 == 0:
            is_leap += 1
            if year % 100 == 0:
                is_leap -= 1
                if year % 400 == 0:
                    is_leap += 1
        if is_leap == 1:
            if day > 29:
                is_valid -= 1
                print("Invalid day")
                
        else:
            if day > 28:
                is_valid -= 1
                print("Invalid day")
                
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            is_valid -= 1
            print("Invalid day")
    
if is_valid == 3:
    print("Valid date ")