# Program : Encrypt a  specific file
# Description : Allow to encrypt a specific file
# Date : 02/07/22
# Author : Christophe Lagaillarde
# Version : 1.00

from cryptography.fernet import Fernet


def encrypt_specific_file(full_path_of_file_to_encrypt, key: bytes, file_name: str) -> None:
    with open(full_path_of_file_to_encrypt, 'rb') as file:
        data: bytes = file.read()

    fernet: Fernet = Fernet(key)
    encrypted: bytes = fernet.encrypt(data)

    with open('C://Users//Lagaillarde//PycharmProject//encrypt_decrypt_files//encrypted_files//'
              + file_name + '.encrypted', 'wb') as file:
        file.write(encrypted)

    return None


