# ==========================================
# ASSIGNMENT 6: SECURE IMAGE TRANSMISSION
# ==========================================
'''Two users are exchanging the images on an unsecured network. Design a security system to
protect the image from any security attack while transmitting it on the network. '''

# STEP 1: Import the required library
from cryptography.fernet import Fernet

# STEP 2: Generate a secret key
# This key is used for both encryption and decryption
key = Fernet.generate_key()

# STEP 3: Create a cipher object using the secret key
cipher = Fernet(key)

# STEP 4: Read the original image
# "rb" means read binary mode
with open("image.png", "rb") as file:
    image_data = file.read()

# STEP 5: Encrypt the image data
# Convert the original image into encrypted data
encrypted_image = cipher.encrypt(image_data)

# STEP 6: Save the encrypted image
# "wb" means write binary mode
with open("encrypted_image.txt", "wb") as file:
    file.write(encrypted_image)

print("Image Encrypted Successfully!")

# STEP 7: Decrypt the encrypted image
# Use the same secret key to recover the original image
decrypted_image = cipher.decrypt(encrypted_image)

# STEP 8: Save the decrypted image
with open("decrypted_image.jpg", "wb") as file:
    file.write(decrypted_image)

print("Image Decrypted Successfully!")

# STEP 9: Display completion message
print("Secure Image Transmission Completed!")