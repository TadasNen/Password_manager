from cryptography.fernet import Fernet
import os.path

def generate_key():
    if os.path.exists("secret.key"):
        pass
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def fernet_encryption(x):
    Key = load_key()
    fernet = Fernet(Key)
    encrypted_password = fernet.encrypt(x.encode())
    return encrypted_password

def fernet_decryption(y):
    Key = load_key()
    fernet = Fernet(Key)
    decrypted_password = fernet.decrypt(y).decode('utf-8')
    return decrypted_password

