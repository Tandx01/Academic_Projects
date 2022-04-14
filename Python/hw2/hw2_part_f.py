"""
Name: Taha Andac
ID : 75785
Section : 03"""

def encrypt(x, e, n):

    """Takes three integers, a random integer, public key and product.
    Encrypts the given random integer using public key and product.
    Returns the encrypted value. """

    iteration = 1
    remainder = x%n

    while iteration != e:
        remainder = (remainder*x)%n
        iteration += 1

    return remainder

def decrypt(y,d,n):

    """Takes three integers, a random integer, public key and product.
    Decrypts the given random integer using public key and product.
    Returns the decrypted value. """

    iteration = 1
    remainder = y%n

    while iteration != d:
        remainder = (remainder*y)%n
        iteration += 1

    return remainder

