# Program : Generate key usigng password
# Description : Allow to get generate a cryptographic key using a password
# Date : 01/07/22
# Author : Christophe Lagaillarde
# Version : 1.0

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from numba import jit
import warnings
import hashlib

warnings.simplefilter('ignore')


@jit
def generate_key_using_password(password: str) -> bytes:
    hashed_password: str = hashlib.sha256(password.encode('utf-8')).hexdigest()

    password_in_bytes: bytes = hashed_password.encode()

    salt = b'\xb9\x82\x83(TQ\xf3\xfd\xc8\xf3=\xc2\xc0{b&'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_in_bytes))  # Can only use kdf once

    return key


if __name__ == '__main__':
    generate_key_using_password()