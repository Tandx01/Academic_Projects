"""
Name: Taha Andac
ID : 75785
Section : 03"""

from hw2_part_a import is_prime

def calculate_n_and_phi():

    """Takes two prime numbers and checks whether they are prime or not.
    If both are prime, calculates product and totient of the numbers. 
    Returns toitent and product"""

    num_1 = int(input("First prime number: "))

    while num_1 < 0 or is_prime(num_1) != 1 :
        num_1 = int(input("Invalid prime, enter again: "))

    num_2 = int(input("Second prime number: "))

    while num_2 < 0 or is_prime(num_2) != 1:
        num_2 = int(input("Invalid prime, enter again: "))

    n = num_1 * num_2
    phi = (num_1-1)*(num_2-1)
    return n, phi
