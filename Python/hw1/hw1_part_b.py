"""
Name: Taha Andac
ID : 75785
Section : 03"""

# Shows number of days, of a month.
# Controls whether months has 30 days or 31
# For february checks whether if it has 28 days or 29 days by controllig leap year.

month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

# is_leap variable checks whether a year is leap or not.

is_leap = 0

if month == 2:
    day = 28
    if year % 4 == 0:
        is_leap += 1
        if year % 100 == 0:
            is_leap -= 1
            if year % 400 == 0:
                is_leap += 1
        if is_leap == 1:
            day = 29
            
elif month == 4 or month == 6 or month == 9 or month == 11:
    day = 30
    
else:
    day = 31
    
print("Number of days ", day)

