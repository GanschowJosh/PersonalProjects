"""
Coded to solve a CTF: given p, q, and e, decrypt encrypted AES message
"""

from sympy import mod_inverse

#given p, q, and e, decrypt AES 
# given values
p = int(input("Enter p:\t"))
q = int(input("Enter q:\t"))
e = int(input("Enter e:\t"))
encrypted_message = list(map(int, input("Enter encrypted numbers, separated by space:\n").split()))

# calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# calculate d
d = mod_inverse(e, phi)

# decrypt message
decrypted_message = [pow(c,d,n) for c in encrypted_message]

# print decrypted message as characters
print("Decrypted Message:\t" + ''.join(chr(m) for m in decrypted_message))

