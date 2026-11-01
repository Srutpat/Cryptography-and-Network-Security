
from cryptography.fernet import Fernet

# Generate secret key
key = Fernet.generate_key()
cipher = Fernet(key)

# Read original image
with open("image.png", "rb") as file:
    image_data = file.read()

# Encrypt image
encrypted_image = cipher.encrypt(image_data)

# Save encrypted image
with open("encrypted_image.txt", "wb") as file:
    file.write(encrypted_image)

print("Image Encrypted Successfully!")

# Decrypt image
decrypted_image = cipher.decrypt(encrypted_image)

# Save decrypted image
with open("decrypted_image.jpg", "wb") as file:
    file.write(decrypted_image)

print("Image Decrypted Successfully!")
