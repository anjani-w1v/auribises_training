# 1assignment -> == vs is explore when these wrk 

# 2Assignment -> explore below
# a)AES, SHA-256 etc are the security algorithms 
# b)which uses shifts and bitwise operations


# ————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————

# #1
# #| `==`                         | `is`                                              |
# # | ---------------------------- | ------------------------------------------------- |
# # | Compares **values**          | Compares **object identity (memory address)**     |
# # | Checks if contents are equal | Checks if both variables refer to the same object |
# # | Uses `__eq__()` internally   | Uses `id()` internally                            |

# # Use == when comparing values.
# # if password == "admin123":
# #     print("Login")
# # Use is when comparing identity, especially with singleton objects like None.
# # if user is None:
# #     print("No user found")


# ————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————


# #bitwise operatrs  &, |, ^, # Shift Operators >>, << ----> used fr security purpses/ encryptin


# ————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————

# #2

# | Algorithm | Purpose    | Used In                                                          |
# | --------- | ---------- | ---------------------------------------------------------------- |
# | AES       | Encryption | Wi-Fi, HTTPS, banking apps, WhatsApp encryption                  |
# | SHA-256   | Hashing    | Password storage, blockchain, digital signatures, file integrity |

# AES is a symmetric encryption algorithm that uses operations like XOR, bit shifts, and substitutions to encrypt data securely.
# SHA-256 is a cryptographic hash algorithm that uses XOR, AND, OR, NOT, and bit shifts/rotations to generate a fixed 256-bit hash. It is commonly used for password hashing, digital signatures, blockchain, and data integrity.

# SHA-256 is a hashing algorithm. Unlike AES, it cannot be decrypted.
#Example: Password = hello123 = 240be518fabd2724ddb6f04eebf2... = Even a tiny change gives a completely different hash.

# AES (Advanced Encryption Standard) is an encryption algorithm. It converts plain text into cipher text so that no one can read it without the secret key.
# Example: HELLO = AES Encryption + Secret Key = Cipher Text = x7A!9kP# = Only someone with the correct key can decrypt it.