# Program : secure delete file
# Description : Allow delete a file in a secure way
# Date : 03/07/22
# Author : Christophe Lagaillarde
# Version : 1.0

import logging
import os
from sys import argv


def secure_delete_file(file_to_delete: str) -> None:
    directory: str = 'C://Users//Lagaillarde//PycharmProject//encrypt_decrypt_files//unencrypted_files//'

    try:
        with open(directory + file_to_delete, 'wb') as file:
            file.write(b'\x00')

            file.close()

        if os.path.exists(directory + file_to_delete):
            os.remove(directory + file_to_delete)

    except FileNotFoundError:
        logging.error('File not existing')

    return None


if __name__ == '__main__':
    secure_delete_file(argv[1])
