"""
Name: Taha Andac
ID : 75785
Section : 03"""

# Calculates how much day passed and left, in given year

day= int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

# tot_sum holds the days passed.
tot_sum = 0
# is_leap checks for leap years.
is_leap = 0

if year % 4 == 0:
    is_leap += 1
    if year % 100 == 0:
        is_leap -= 1
        if year % 400 == 0:
            is_leap += 1


for i in range(1,month):
    if i == 2:
        if is_leap == 1:
            tot_sum += 29
        else:
            tot_sum += 28
    elif i == 4 or i == 6 or i == 9 or i == 11:
        tot_sum += 30
    else:
        tot_sum += 31

tot_sum += day

if is_leap == 1:
    day_left = 366 - tot_sum
else:
    day_left = 365 - tot_sum
    
print("Days passed: ", tot_sum)
print("Days left: ", day_left)