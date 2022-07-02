# Program : Encrypt a file or a folder
# Description : Allow to encrypt a file or a folder
# Date : 01/07/22
# Author : Christophe Lagaillarde
# Version : 2.00

import logging
from sys import argv
from os import path
import os
from generate_key_using_password import generate_key_using_password
from encrypt_specific_file import encrypt_specific_file


def encrypt(path_to_encrypt: str) -> None:

    if path.exists(path_to_encrypt):
        is_file: bool = os.path.isfile(path_to_encrypt)

        key: bytes = generate_key_using_password()

        if is_file:
            file_name: str = os.path.basename(path_to_encrypt)
            encrypt_specific_file(path_to_encrypt, key, file_name)

        else:
            for filename in os.listdir(path_to_encrypt):
                specific_file_to_encrypt: str = os.path.join(path_to_encrypt, filename)
                if os.path.isfile(specific_file_to_encrypt):
                    encrypt_specific_file(specific_file_to_encrypt, key, filename)

    else:
        logging.error('file or folder does not exist')

    return None


if __name__ == '__main__':
    encrypt(argv[1])
