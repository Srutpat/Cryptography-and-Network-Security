
# ==========================================
# ASSIGNMENT 5: DIFFIE-HELLMAN MITM ATTACK 
# ==========================================
'''Demonstrate how Diffie-Hellman key exchange works with Man-In-The-Middleattack.
Two employees of a financial company, Alice and Bob, want to exchange confidential messages
securely over the internet. They decide to use the Diffie-Hellman (DH) key exchange algorithm to
generate a shared secret key. However, the company‘s network is being monitored by a malicious
attacker, Eve. Since DH alone does not provide authentication, Eve is able to launch a Man-inthe-Middle (MITM) attack by intercepting and modifying the key exchange messages.
Demonstrate how the DH key exchange works and how it can be exploited by a MITM attack,
Also propose solutions to mitigate the attack'''

# STEP 1: Import secrets module

import secrets


# STEP 2: Define public parameters

p = 23
g = 5


# STEP 3: Generate private keys randomly

a = secrets.randbelow(p - 3) + 2
b = secrets.randbelow(p - 3) + 2

e1 = secrets.randbelow(p - 3) + 2
e2 = secrets.randbelow(p - 3) + 2


# STEP 4: Calculate Alice's and Bob's public keys

A = pow(g, a, p)
B = pow(g, b, p)

print("Alice Public Key:", A)
print("Bob Public Key:", B)


# STEP 5: Eve generates two public values

E1 = pow(g, e1, p)
E2 = pow(g, e2, p)

print("Eve sends E1 to Alice:", E1)
print("Eve sends E2 to Bob:", E2)


# STEP 6: Alice and Bob calculate shared keys

alice_key = pow(E1, a, p)
bob_key = pow(E2, b, p)


# STEP 7: Eve calculates shared keys

eve_alice_key = pow(A, e1, p)
eve_bob_key = pow(B, e2, p)


# STEP 8: Display shared keys

print("Alice's Shared Key:", alice_key)
print("Bob's Shared Key:", bob_key)

print("Eve's Key with Alice:", eve_alice_key)
print("Eve's Key with Bob:", eve_bob_key)


# STEP 9: Verify MITM attack

if alice_key == eve_alice_key and bob_key == eve_bob_key:

    print("MITM Attack Successful!")

else:

    print("MITM Attack Failed!")