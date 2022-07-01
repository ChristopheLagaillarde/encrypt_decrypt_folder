# Program : Generate cryptographic key
# Description : Allow to generate cryptographic key inside of a file
# Date : 01/07/22
# Author : Christophe Lagaillarde
# Version : 1.0

from sys import argv
from cryptography.fernet import Fernet


def generate_key_in_file() -> None:
    key_name: str = argv[1]
    key = Fernet.generate_key()
    file = open(key_name + '.key', 'wb')
    file.write(key)
    file.close()

    return None


if __name__ == '__main__':
    generate_key_in_file()