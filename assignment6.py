
# ==========================================
# ASSIGNMENT 5: DIGITAL SIGNATURE (DSS)
# ==========================================

# STEP 1: Import required libraries

from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


# STEP 2: Generate private key

private_key = dsa.generate_private_key(key_size=2048)


# STEP 3: Generate corresponding public key

public_key = private_key.public_key()


# STEP 4: Take message input

# encode() converts string into bytes

message = input("Enter message: ").encode()


# STEP 5: Generate digital signature

# Private key is used to sign the message
# SHA-256 is used as the hashing algorithm

signature = private_key.sign(message, hashes.SHA256())


# STEP 6: Display generated signature

print("\nDigital Signature Generated!")

print("Signature:", signature.hex())


# STEP 7: Verify digital signature

# Public key is used to verify the signature

try:

    public_key.verify(signature, message, hashes.SHA256())

    print("\nSignature is Valid!")


# STEP 8: Handle invalid signature

except InvalidSignature:

    print("\nSignature is Invalid!")
