import os
from aes_pin_chipping import derive_aes_key_from_pin
from Cryptodome.Cipher import AES
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA256
import tkinter as tk
from tkinter import filedialog

from rsa_generation import generate_rsa_key_pair

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

def encrypt_private_key(private_key, aes_key):
    private_key_bytes = private_key.encode('utf-8')
    pad_length = AES.block_size - (len(private_key_bytes) % AES.block_size)
    padded_private_key = private_key_bytes + bytes([pad_length] * pad_length)
    cipher = AES.new(aes_key, AES.MODE_CBC, iv=bytes([0] * 16))
    encrypted_private_key = cipher.encrypt(padded_private_key)

    return encrypted_private_key


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
    public_key, private_key = generate_rsa_key_pair()
    document = load_document()
    if document:
        signature = sign_document(private_key, document)
        aes_key = derive_aes_key_from_pin(EXAMPLE_PIN)
        encrypted_private_key = encrypt_private_key(private_key, aes_key)
        save_to_pendrive(encrypted_private_key)
    else:
        print("No document selected or document loading failed.")

if __name__ == "__main__":
    main()
