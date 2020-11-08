from math import gcd

def brute_force_trail():
    
    plaintext = 99213341
    
    # random prime number (128 bits)
    p = 74843584674326699817347547769510352269
    q = 105025942399604912498174223214224846707
    
    # public key
    n = p*q
    e = 3
    
    encrypted_message = plaintext**e % n

    for x in range (0,1_000_000_000):
        if encrypted_message == x**e % n:
            print('The original message is {}'.format(x))
            break
    else:
        print('Not found!')
        
bf = brute_force_trail()
