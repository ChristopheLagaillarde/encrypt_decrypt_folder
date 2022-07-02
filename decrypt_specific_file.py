# Program :
# Description :
# Date :
# Author : Christophe Lagaillarde
# Version : 1.0

import logging

import cryptography
from cryptography.fernet import Fernet


def decrypt_specific_file(file_to_decrypt: str, key: bytes, file_name) -> None:

    try:
        with open(file_to_decrypt, 'rb') as file:
            data = file.read()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)

        with open('C://Users//Lagaillarde//PycharmProject//encrypt_decrypt_files//unencrypted_files//'
                  + file_name, 'wb') as file:
            file.write(decrypted)

    except cryptography.fernet.InvalidToken:
        logging.error('Invalid password')

    return None
