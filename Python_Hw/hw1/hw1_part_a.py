"""
Name: Taha Andac
ID : 75785
Section : 03"""

# Controls whether a year is leap year or not.
# If year is leap prints Leap year, if not prints Not leap year.

year = int(input(" Enter a year: "))

# is_leap is the variable that checks leap years. 

is_leap=0

if year % 4 == 0 :
    is_leap +=1
    if year % 100 == 0:
        is_leap -=1
        if year % 400 == 0:
            is_leap +=1

if is_leap == 1:
    print(" Leap year ")
else:
    print(" Not leap year ")
