# ==========================================
# ASSIGNMENT 4: XOR ENCRYPTION AND DECRYPTION
# ==========================================
'''Design and Implement your own encryption/decryption algorithm using any programming
language. A start-up company is building a file-sharing system for its employees to exchange sensitive
project documents (like contracts, reports, and source code). They cannot rely on existing
standard algorithms (AES, DES, RSA, etc.) due to licensing and intellectual property concerns.
Design and implement a custom encryption/decryption algorithm in a programming language of
your choice (C, C++, Java, Python, etc.). The algorithm should securely convert plaintext
messages into ciphertext and recover the original message correctly'''
# STEP 1: Take message input from user
message = input("Enter your message: ")
# STEP 2: Define secret encryption key
key = 5
# STEP 3: Create an empty string for encrypted data
encrypted = ""
# STEP 4: Encrypt the message using XOR
for ch in message:
    # ord(ch) converts character into its integer value
    # ^ performs XOR operation with the secret key
    # chr() converts the result back into a character
    encrypted += chr(ord(ch) ^ key)
# Display encrypted message
print("Encrypted Message:", encrypted)
# STEP 5: Create an empty string for decrypted data
decrypted = ""
# STEP 6: Decrypt using the SAME XOR key
for ch in encrypted:
    # XOR with the same key again
    # recovers the original character
    decrypted += chr(ord(ch) ^ key)
# STEP 7: Display decrypted message
print("Decrypted Message:", decrypted)