
# ==========================================
# ASSIGNMENT 4: SHA-1 MESSAGE DIGEST
# AND AVALANCHE EFFECT
# ==========================================

# STEP 1: Import hashing library

import hashlib


# STEP 2: Take message input

message = input("Enter a message: ")


# STEP 3: Generate SHA-1 hash of original message

# encode() converts string into bytes
# sha1() generates the hash
# hexdigest() converts hash into hexadecimal format

hash_value = hashlib.sha1(message.encode()).hexdigest()


# STEP 4: Display original message and hash

print("\nOriginal Message:", message)
print("SHA-1 Hash:", hash_value)


# STEP 5: Modify the original message

# Add one character to the original message

modified_message = message + "A"


# STEP 6: Generate hash of modified message

modified_hash = hashlib.sha1(
    modified_message.encode()
).hexdigest()


# STEP 7: Display modified message and hash

print("\nModified Message:", modified_message)
print("Modified Hash:", modified_hash)


# STEP 8: Compare both hash values

if hash_value != modified_hash:

    print("\nMessage has been modified!")
    print("Avalanche Effect Demonstrated!")

else:

    print("\nHashes are identical.")
