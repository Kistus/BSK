from document_sign import *
from aes_pin_chipping import derive_aes_key_from_pin
from Cryptodome.Cipher import AES
import os


def main():
    public_key, private_key = generate_rsa_key_pair()
    document = load_document()
    signature = sign_document(private_key, document)

    aes_key = derive_aes_key_from_pin(private_key)

    def encrypt_private_key(private_key, aes_key):
        # Pad the private key to be a multiple of 16 bytes (AES block size)
        private_key_padded = private_key + (16 - len(private_key) % 16) * ' '
        cipher = AES.new(aes_key, AES.MODE_ECB)  # Use ECB mode for simplicity
        encrypted_private_key = cipher.encrypt(private_key_padded.encode('utf-8'))
        return encrypted_private_key

    # Function to save the encrypted private key to the pendrive
    def save_to_pendrive(encrypted_private_key, pendrive_path):
        with open(pendrive_path, 'wb') as file:
            file.write(encrypted_private_key)

    # Example usage
    private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDXEj3fo2Tc+1aI\n+5zDnXa3mKbOzNYD..."
    pin = "1234"  # Example PIN number
    aes_key = derive_aes_key_from_pin(pin)

    # Encrypt the private key using AES
    encrypted_private_key = encrypt_private_key(private_key, aes_key)

    # Save the encrypted private key to the pendrive
    pendrive_path = "D:/private_key_encrypted.bin"  # Example pendrive path
    save_to_pendrive(encrypted_private_key, pendrive_path)


if __name__ == "__main__":
    main()
