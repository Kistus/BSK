import os

from document_sign import generate_rsa_key_pair
from aes_pin_chipping import derive_aes_key_from_pin
from Cryptodome.Cipher import AES
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA256
import tkinter as tk
from tkinter import filedialog

# Constants
EXAMPLE_PIN = "1234"

def sign_document(private_key, document):
    key = RSA.import_key(private_key)
    signer = PKCS1_v1_5.new(key)
    hash_obj = SHA256.new(document)
    signature = signer.sign(hash_obj)
    return signature

def load_document():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'rb') as file:
            document = file.read()
        return document
    else:
        return None


# Function to encrypt the private key using AES
# Function to encrypt the private key using AES with PKCS7 padding
# Function to encrypt the private key using AES with PKCS7 padding
def encrypt_private_key(private_key, aes_key):
    # Convert private key to bytes
    private_key_bytes = private_key.encode('utf-8')

    # Pad the private key using PKCS7 padding
    pad_length = AES.block_size - (len(private_key_bytes) % AES.block_size)
    padded_private_key = private_key_bytes + bytes([pad_length] * pad_length)

    # Create AES cipher object
    cipher = AES.new(aes_key, AES.MODE_CBC, iv=bytes([0] * 16))

    # Encrypt the padded private key
    encrypted_private_key = cipher.encrypt(padded_private_key)

    return encrypted_private_key


# Function to save the encrypted private key to the pendrive
def save_to_pendrive(encrypted_private_key):
    root = tk.Tk()
    root.withdraw()
    pendrive_path = filedialog.askdirectory(title="Select Pendrive")
    if pendrive_path:
        pendrive_path = os.path.join(pendrive_path, "private_key_encrypted.bin")
        with open(pendrive_path, 'wb') as file:
            file.write(encrypted_private_key)
        print("Private key encrypted and saved to pendrive:", pendrive_path)
    else:
        print("No pendrive selected.")

def main():
    # Generate RSA key pair
    public_key, private_key = generate_rsa_key_pair()

    # Load document
    document = load_document()

    if document:
        # Sign document
        signature = sign_document(private_key, document)

        # Derive AES key from PIN
        aes_key = derive_aes_key_from_pin(EXAMPLE_PIN)

        # Encrypt private key using AES
        encrypted_private_key = encrypt_private_key(private_key, aes_key)

        # Save encrypted private key to pendrive
        save_to_pendrive(encrypted_private_key)
    else:
        print("No document selected or document loading failed.")

if __name__ == "__main__":
    main()
