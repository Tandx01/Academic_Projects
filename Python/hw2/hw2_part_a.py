"""
Name: Taha Andac
ID : 75785
Section : 03"""

from math import sqrt

def is_prime (number):

    """Takes a integer and returns True if the integer is prime
    and returns False otherwise"""

    sqrt_number = int(sqrt (number))

    for i in range (2, sqrt_number+1):
        if number % i == 0:
            return False
    return True

def is_relatively_prime(first, second):

    """Takes two integers and returns True if the two integers are
    relatively prime and returns False otherwise. """

    first_num = first
    second_num = second
    if second_num > first_num:
        (first_num, second_num)=(second_num,first_num)

    while second_num !=0 :
        module_1 = first_num%second_num
        first_num = second_num
        second_num = module_1
    if first_num == 1:
        return True 
    return False
