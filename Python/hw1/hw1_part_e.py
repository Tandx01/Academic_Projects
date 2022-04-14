"""
Name: Taha Andac
ID : 75785
Section : 03"""

# Takes two dates from user, one is birth date other is current date.
# Calculates day differance between them.
# Prints how much the user has lived between given dates.

cur_day = int(input("Enter the current day: "))
cur_month = int(input("Enter the current month: "))
cur_year = int(input("Enter the current year: "))
birth_day = int(input("Enter the date of birth day: "))
birth_month = int(input("Enter the date of birth month: "))
birth_year = int(input("Enter the date of birth year: "))

# Day lived holds day number from given birth year to given current date.
day_lived = 0
# minus_day holds day number between given birth date and given birth year.
# at the end of code this value is subtracted from day_lived.
minus_day = 0

for year in range(birth_year, cur_year):

    is_leap = 0
    
    if year % 4 == 0 :
        is_leap +=1
        if year % 100 == 0:
            is_leap -=1
            if year % 400 == 0:
                is_leap +=1
    
    if is_leap == 1:
        day_lived += 366
        
    else:
        day_lived += 365
        
is_leap = 0

if birth_year % 4 == 0 :
    is_leap +=1
    if birth_year % 100 == 0:
        is_leap -=1
        if birth_year % 400 == 0:
            is_leap +=1

for month in range(1,birth_month):
    if month == 2:
        if is_leap == 1:
            minus_day += 29
        else:
            minus_day += 28
            
    elif month == 4 or month == 6 or month == 9 or month == 11:
        minus_day += 30
        
    else:
        minus_day +=31
            
minus_day += birth_day

is_leap = 0

if cur_year % 4 == 0 :
    is_leap +=1
    if cur_year % 100 == 0:
        is_leap -=1
        if cur_year % 400 == 0:
            is_leap +=1

for month in range(1,cur_month):
    if month == 2:
        if is_leap == 1:
            day_lived += 29
        else:
            day_lived += 28
            
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day_lived += 30
        
    else:
        day_lived +=31
            
day_lived += cur_day

day_lived = (day_lived-minus_day)

print("You have lived ",day_lived, "days")