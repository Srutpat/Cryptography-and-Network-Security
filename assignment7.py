# ==========================================
# ASSIGNMENT 5: DIGITAL SIGNATURE USING DSS
# ==========================================


# STEP 1: Import required libraries

from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


# STEP 2: Generate DSA private key

private_key = dsa.generate_private_key(key_size=2048)


# STEP 3: Generate public key from private key

public_key = private_key.public_key()


# STEP 4: Accept message from user

# encode() converts string into bytes

message = input("Enter message: ").encode()


# STEP 5: Generate digital signature using private key

# SHA256 is used to generate the message digest

signature = private_key.sign(message, hashes.SHA256())


# STEP 6: Display generated digital signature

print("Digital Signature Generated!")

print("Signature:", signature.hex())


# STEP 7: Verify digital signature using public key

try:

    public_key.verify(signature, message, hashes.SHA256())

    print("Signature is Valid!")


# STEP 8: Handle invalid signature

except InvalidSignature:

    print("Signature is Invalid!")