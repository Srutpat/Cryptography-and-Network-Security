
# ==========================================
# ASSIGNMENT 3: RSA PERFORMANCE ANALYSIS
# ==========================================
'''Design an experiment to estimate the amount of time to i) Generate key pair (RSA) ii) Encrypt n
bit message (RSA) iii) Decrypt n bit message (RSA) As function of key size, experiment with
different n-bit messages. Summarize your conclusions '''

# STEP 1: Import required libraries

import time
import os

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# STEP 2: Define different RSA key sizes and message sizes

key_sizes = [1024, 2048, 3072]

# Message sizes are in bits
message_sizes = [64, 128, 256, 384]


# STEP 3: Repeat experiment for each RSA key size

for key_size in key_sizes:

    # Start measuring key generation time
    start = time.perf_counter()

    # Generate 5 RSA key pairs to calculate average time
    for i in range(5):

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size
        )

    # Calculate average key generation time
    key_time = (time.perf_counter() - start) / 5

    # Extract public key from private key
    public_key = private_key.public_key()

    print("\nRSA Key Size:", key_size)
    print("Key Generation Time:", key_time * 1000, "ms")


    # STEP 4: Test different message sizes

    for bits in message_sizes:

        # Generate random message
        # Divide by 8 because 1 byte = 8 bits
        message = os.urandom(bits // 8)


        # STEP 5: Configure OAEP padding with SHA-256

        oaep = padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )


        # STEP 6: Measure encryption time

        start = time.perf_counter()

        # Encrypt message 100 times using public key
        for i in range(100):

            ciphertext = public_key.encrypt(message, oaep)

        # Calculate average encryption time
        encrypt_time = (time.perf_counter() - start) / 100


        # STEP 7: Measure decryption time

        start = time.perf_counter()

        # Decrypt ciphertext 100 times using private key
        for i in range(100):

            decrypted = private_key.decrypt(ciphertext, oaep)

        # Calculate average decryption time
        decrypt_time = (time.perf_counter() - start) / 100


        # STEP 8: Display results

        print("\nMessage Size:", bits, "bits")

        print("Encryption Time:",
              encrypt_time * 1000, "ms")

        print("Decryption Time:",
              decrypt_time * 1000, "ms")


        # STEP 9: Verify decrypted message

        assert decrypted == message

        print("Message Verification Successful!")


# STEP 10: End of experiment

print("\nExperiment Completed!")
