import re

from Encryption import *


def encrypt_message(raw_text) -> tuple[str, str]:
    encryption_key = ""
    encrypted_message = ""
    words = re.findall(regex_search_pattern, raw_text)
    for group in words:
        sep_char = group[1]
        current_word = group[0]
        word = OneTimePad(current_word)
        encrypted_word, word_key = word.encrypt_word()
        encrypted_message += encrypted_word + sep_char
        encryption_key += word_key + sep_char
    return encrypted_message, encryption_key


def decrypt_message(encrypted_text, key) -> str:
    decrypted_messsage = ""
    words = re.findall(regex_search_pattern, encrypted_text)
    keys = re.findall(regex_search_pattern, key)
    for index in range(len(words)):
        sep_char = words[index][1]
        current_word = words[index][0]
        current_key = keys[index][0]
        word = OneTimePad(current_word)
        decrypted_messsage += word.decrypt_word(current_word, current_key) + sep_char
    return decrypted_messsage


def print_output():
    print("Initial message is:", user_text)
    print("Encrypted message is:", encrypted_message)
    print("Encryption Key is:", encryption_key)
    print("Decrypted message is:", decrypted_message)


regex_search_pattern = r"(\w+)(.?)"
user_text = "huh,interesting!"

encrypted_message, encryption_key = encrypt_message(user_text)
decrypted_message = decrypt_message(encrypted_message, encryption_key)

print_output()
