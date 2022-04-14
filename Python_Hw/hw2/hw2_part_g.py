"""
Name: Taha Andac
ID : 75785
Section : 03"""

import hw2_part_b
import hw2_part_c
import hw2_part_d
import hw2_part_e
import hw2_part_f

def main ():

    """Allows user to generate public keys and private keys.
    User can encrypt and decrypt random integers with using generated keys
    or user can close the program if they wish.
     """

    keys_generated = False
    choice = hw2_part_b.display_menu()
    while choice != 'X':

        if choice == 'G':
            n, phi = hw2_part_c.calculate_n_and_phi()
            e, n = hw2_part_d.generate_public_key(n, phi)
            d, n = hw2_part_e.generate_private_key(e, n, phi)
            keys_generated = True
            print('Keys have been generated')
            print('Public key: (', e, ', ', n, ')', sep = '')
            print('Private key: (', d, ', ', n, ')', '\n', sep = '')
            
            

        elif choice == 'E':
            if not keys_generated:
                print('You need to generate the keys before encryption\n')
                
            else:
                x = int(input('Enter the message to be encrypted: '))
                y = hw2_part_f.encrypt(x, e, n)
                print(x, 'is encrypted as', y, '\n')
                

        elif choice == 'D':
            if not keys_generated:
                print('You need to generate the keys before decryption', '\n')
                
            else:
                y = int(input('Enter the message to be decrypted: '))
                x = hw2_part_f.decrypt(y, d, n)
                print(y, 'is decrypted as', x, '\n')
                
        choice = hw2_part_b.display_menu()
            
    print ("Terminating program...")

main()