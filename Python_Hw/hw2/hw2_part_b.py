"""
Name: Taha Andac
ID : 75785
Section : 03"""

def display_menu():

    """Displays a menu for the choice of a user and returns that choice."""

    print("g or G for key generation")
    print("e or E for encrytion")
    print("d or D for decryption")
    print("x or X to exit")

    option = input("Please enter your choice: ")

    while option != 'g' and option != 'G'and option != 'e' and option != 'E' and option != 'd' and option != 'D' and option != 'x' and option != 'X':

        print('\n   ***Invalid option***   \n ')

        print("g or G for key generation")
        print("e or E for encrytion")
        print("d or D for decryption")
        print("x or X to exit")

        option = input("Please enter your choice: ")
    else:
        if option == 'g' or option == 'G':
            option = 'G'
        elif option == 'e' or option == 'E':
            option = 'E'
        elif option == 'd' or option == 'D':
            option = 'D'
        else:
            option = 'X'

        return option

