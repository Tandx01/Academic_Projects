"""
Name: Taha Andac
ID : 75785
Section : 03"""

def generate_private_key(e, n, phi):

    """Takes three integers public key, product and totient.
    Generates a private key using public key and totient.
    Returns private key and product."""

    m = 0
    while (1+m*phi)% e != 0:
        m+=1
    d = ((1+m*phi)/e)
    return int(d), n
