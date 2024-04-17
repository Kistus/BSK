from Cryptodome.PublicKey import RSA

def generate_rsa_key_pair():
    key = RSA.generate(4096)
    public_key = key.publickey().export_key().decode('utf-8')
    private_key = key.export_key().decode('utf-8')

    return public_key, private_key

public_key, private_key = generate_rsa_key_pair()

