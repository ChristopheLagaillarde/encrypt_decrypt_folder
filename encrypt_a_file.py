# Program : Encrypt a file
# Description : Allow to encrypt a file
# Date : 01/07/22
# Author : Christophe Lagaillarde
# Version : 1.00

from sys import argv
from cryptography.fernet import Fernet
from generate_key_using_password import generate_key_using_password


def encrypt_a_file(file_name: str, password: str) -> None:

    key: bytes = generate_key_using_password(password)

    with open(file_name, 'rb') as file:
        data: bytes = file.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(file_name + '.encrypted', 'wb') as file:
        file.write(encrypted)

    return None


if __name__ == '__main__':
    encrypt_a_file(argv[1], argv[2])
