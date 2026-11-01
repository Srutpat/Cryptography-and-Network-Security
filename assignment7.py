
# ==========================================
# ASSIGNMENT 6: SECURE IMAGE TRANSMISSION
# ==========================================

# STEP 1: Import Fernet encryption library

from cryptography.fernet import Fernet


# STEP 2: Generate a secret encryption key

key = Fernet.generate_key()


# STEP 3: Create encryption object using the key

cipher = Fernet(key)


# STEP 4: Open and read the original image

# rb = Read Binary mode
# Images must be read as binary data

with open("image.jpg", "rb") as file:

    image_data = file.read()


# STEP 5: Encrypt the image data

encrypted_image = cipher.encrypt(image_data)


# STEP 6: Save encrypted image data into a file

# wb = Write Binary mode

with open("encrypted_image.txt", "wb") as file:

    file.write(encrypted_image)

print("Image Encrypted Successfully!")


# STEP 7: Decrypt the encrypted image

decrypted_image = cipher.decrypt(encrypted_image)


# STEP 8: Save the decrypted image

with open("decrypted_image.jpg", "wb") as file:

    file.write(decrypted_image)

print("Image Decrypted Successfully!")


# STEP 9: Display completion message

print("Secure Image Transmission Completed!")
