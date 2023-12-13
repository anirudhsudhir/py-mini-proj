import pytest

from Tokenize import *


def test_encrypt_decrypt_text():
    user_text = "HUH,INTERESTING!"
    encrypted_message, encryption_key = encrypt_message(user_text)
    decrypted_message = decrypt_message(encrypted_message, encryption_key)
    assert user_text == decrypted_message
