import hashlib

def derive_aes_key_from_pin(pin):
    pin_bytes = pin.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(pin_bytes)
    aes_key = sha256.digest()

    return aes_key


