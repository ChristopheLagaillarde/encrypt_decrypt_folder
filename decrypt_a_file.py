# Program : Decrypt a file
# Description : Allow to decrypt a file
# Date : 01/07/22
# Author : Christophe Lagaillarde
# Version : 1.00
from sys import argv

from cryptography.fernet import Fernet
import cryptography.fernet
import logging
from generate_key_using_password import generate_key_using_password


def decrypt_a_file(file_name: str, password: str) -> None:
    key: bytes = generate_key_using_password(password)

    try:
        with open(file_name + '.encrypted', 'rb') as file:
            data = file.read()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)

        with open('decrypted_' + file_name, 'wb') as file:
            file.write(decrypted)

    except cryptography.fernet.InvalidToken:
        logging.error('Invalid password')

    return None


if __name__ == '__main__':
    decrypt_a_file(argv[1], argv[2])
