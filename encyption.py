from cryptography.fernet import Fernet
import os.path


def generate_key():
    """
    Function creates key and file containing it for first time users.
    If the file already exists (for user who already used the program), key will be reused.
    Function used in main.py everytime it program is activated.
    :return: if -> None, else -> secret.key file
    """
    if os.path.exists("secret.key"):
        pass
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)


def load_key():
    """
    Function reads key from secret.key file
    :return: returns key located in secret.key file
    """
    return open("secret.key", "rb").read()


def fernet_encryption(x: str) -> bytes:
    """
    Function calls load_key function and loads key used for x encryption
    :param x:  Variable containing string of password. Variable during encryption is converted to bytes for Fernet
    encryption library to work
    :return: Returns encrypted x variable/password
    """
    Key = load_key()
    fernet = Fernet(Key)
    encrypted_password = fernet.encrypt(x.encode())
    return encrypted_password


def fernet_decryption(y: bytes) -> str:
    """
    Functioon calls load_key function and loads key used for y decryption
    :param y: Variable containing string of bytes that decrypts password. Variable during dencryption is
    converted to UTF-8 coding and returns string
    :return:
    """
    Key = load_key()
    fernet = Fernet(Key)
    decrypted_password = fernet.decrypt(y).decode('utf-8')
    return decrypted_password
