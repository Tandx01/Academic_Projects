"""
Name: Taha Andac
ID : 75785
Section : 03"""

from hw2_part_a import is_relatively_prime

def generate_public_key(n, phi):

    """Takes two inetegers, product and totient. Generates a public key which is
    relatively prime with totient. Returns public key and product. """

    e = 2
    while is_relatively_prime(e, phi) != 1:
        e+=1
    return e,n

