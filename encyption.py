from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

def fernet_encryption(x):
    encrypted_password = fernet.encrypt(x)
    return encrypted_password

def fernet_decryption(y):
    decrypted_password = fernet.decrypt(y)
    return decrypted_password