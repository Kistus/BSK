import hashlib


def derive_aes_key_from_pin(pin):
    """
    Derive AES key from the user's PIN number using SHA-256 hash function.

    Args:
        pin (str): User's PIN number.

    Returns:
        bytes: Derived AES key.
    """
    # Convert PIN to bytes
    pin_bytes = pin.encode('utf-8')

    # Hash the PIN using SHA-256
    sha256 = hashlib.sha256()
    sha256.update(pin_bytes)
    aes_key = sha256.digest()

    return aes_key


# Test the AES key derivation function
pin = "1234"  # Example PIN number
aes_key = derive_aes_key_from_pin(pin)
print("Derived AES Key:", aes_key)



# Function to encrypt the private key using AES
