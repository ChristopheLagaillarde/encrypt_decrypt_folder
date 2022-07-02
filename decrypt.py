# Program : Decrypt a file or folder
# Description : Allow to decrypt a file or folder
# Date : 01/07/22
# Author : Christophe Lagaillarde
# Version : 2.00

from sys import argv
from os import path
import os
import logging
from generate_key_using_password import generate_key_using_password
from decrypt_specific_file import decrypt_specific_file


def decrypt(path_to_decrypt: str) -> None:

    if path.exists(path_to_decrypt):
        is_file: bool = os.path.isfile(path_to_decrypt)

        key: bytes = generate_key_using_password()

        if is_file:
            file_name: str = os.path.basename(path_to_decrypt)[:-9]  # to remove .encrypted extension

            decrypt_specific_file(path_to_decrypt, key, file_name)

        else:
            for filename in os.listdir(path_to_decrypt):
                specific_file_to_decrypt: str = os.path.join(path_to_decrypt, filename)
                if os.path.isfile(specific_file_to_decrypt):
                    decrypt_specific_file(specific_file_to_decrypt, key, filename[:-9])

    else:
        logging.error('file or folder does not exist')

    return None


if __name__ == '__main__':
    decrypt(argv[1])
