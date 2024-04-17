from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA256
import tkinter as tk
from tkinter import filedialog

from rsa_generation import generate_rsa_key_pair


# Function to sign a document using RSA private key
def sign_document(private_key, document):
    key = RSA.import_key(private_key)
    signer = PKCS1_v1_5.new(key)
    hash_obj = SHA256.new(document)
    signature = signer.sign(hash_obj)
    return signature

# Function to load a document
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
