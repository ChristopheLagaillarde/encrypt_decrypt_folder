# Program : Get key from
# Description : Allow to get the cryptographic key stored in a file
# Date : 01/07/22
# Author : Christophe Lagaillarde
# Version : 1.0

from sys import argv


def get_key_from_file() -> bytes:
    file_name: str = argv[1]
    file = open(file_name + '.key', 'rb')
    key = file.read()
    file.close()

    return key


if __name__ == '__main__':
    get_key_from_file()