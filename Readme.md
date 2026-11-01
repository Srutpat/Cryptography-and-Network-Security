# Cryptography and Network Security Lab Assignments

This repository contains six Python practical assignments for the **Cryptography and Network Security** lab. The programs demonstrate encryption, decryption, key exchange, hashing, digital signatures, and secure image transmission.

## Requirements

- Python 3.x
- `cryptography` Python package

### Install the required package

```bash
pip install cryptography
```

> **Note:** Assignments 2 and 4 use Python's built-in modules and do not require the `cryptography` package. Assignments 1, 3, 5, and 6 use the `cryptography` package.

## Assignments

### 1. RSA Performance Analysis

- Implements RSA encryption and decryption using the OAEP padding scheme.
- Measures key generation, encryption, and decryption time.
- Compares performance for different RSA key sizes and message sizes.
- Uses the `cryptography` package.

### 2. XOR Encryption and Decryption

- Demonstrates a basic symmetric encryption technique using XOR.
- Uses the same secret key for encryption and decryption.
- Shows how applying XOR with the same key twice restores the original message.
- Uses Python's built-in functions; no external package required.

### 3. Diffie-Hellman Key Exchange with Man-in-the-Middle Attack

- Demonstrates the Diffie-Hellman key exchange algorithm.
- Simulates Alice, Bob, and an attacker (Eve).
- Shows how an attacker can intercept and replace public keys to establish separate shared secrets with both parties.
- Uses the `cryptography` package only if your implementation imports it; the basic modular-arithmetic demonstration can run with Python's built-in functions.

### 4. SHA-1 Hashing and Avalanche Effect

- Generates a SHA-1 message digest.
- Modifies the original message and calculates its hash again.
- Demonstrates the avalanche effect, where a small input change produces a significantly different hash.
- Uses Python's built-in `hashlib` module; no external package required.

### 5. Digital Signature using DSS/DSA

- Generates a DSA private and public key pair.
- Creates a digital signature using the private key and SHA-256.
- Verifies the signature using the public key.
- Demonstrates message integrity and signature authentication.
- Uses the `cryptography` package.

### 6. Secure Image Transmission using Fernet

- Reads an image in binary mode.
- Encrypts the image using Fernet symmetric encryption.
- Saves the encrypted data and decrypts it.
- Reconstructs the original image from the decrypted data.
- Uses the `cryptography` package.

**Input file required:** `image.jpg` must be present in the same directory as the Python script.

## Project Structure

```text
Cryptography-and-Network-Security/
│
├── Assignment-1/
│   └── rsa_performance.py
│
├── Assignment-2/
│   └── xor_encryption.py
│
├── Assignment-3/
│   └── diffie_hellman_mitm.py
│
├── Assignment-4/
│   └── sha1_hashing.py
│
├── Assignment-5/
│   └── digital_signature.py
│
├── Assignment-6/
│   ├── secure_image_transmission.py
│   └── image.jpg
│
└── README.md
```

*The filenames and folder structure above are suggested. Adjust them to match the files in your repository.*

## Running the Programs

Navigate to the relevant assignment directory and run:

```bash
python filename.py
```

For example:

```bash
python rsa_performance.py
```

## Important Notes

- These programs are educational demonstrations of cryptographic concepts.
- The XOR implementation uses a fixed key and is **not secure for real-world use**.
- The Diffie-Hellman MITM demonstration uses small sample parameters for learning; real systems require secure parameters and authenticated key exchange.
- SHA-1 is included for learning purposes. It is not recommended for modern security-sensitive applications because of known collision weaknesses. Prefer SHA-256 or stronger.
- The RSA experiment includes a 1024-bit key size for comparison; use at least 2048-bit RSA keys for modern applications.
- The Fernet program generates a key at runtime. For actual communication, the receiver must securely obtain the same key.

## Technologies Used

- Python
- RSA
- XOR
- Diffie-Hellman Key Exchange
- SHA-1
- DSS/DSA Digital Signatures
- Fernet Symmetric Encryption
- `cryptography` library

---

**Purpose:** Academic practical work for the Cryptography and Network Security subject.