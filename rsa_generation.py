from Cryptodome.PublicKey import RSA


def generate_rsa_key_pair():
    """
    Generate RSA key pair for user A.

    Returns:
        tuple: Tuple containing the RSA public key and private key.
    """
    # Generate RSA key pair with a key length of 4096 bits
    key = RSA.generate(4096)

    # Extract public key and private key
    public_key = key.publickey().export_key().decode('utf-8')
    private_key = key.export_key().decode('utf-8')

    return public_key, private_key


# Test the RSA key generation function
public_key, private_key = generate_rsa_key_pair()
print("Public Key:", public_key)
print("Private Key:", private_key)
