import secrets


class OneTimePad:
    def __init__(self, msg):
        self.msg = msg.upper()  # Message to be encrypted or decrypted

    def generate_key(self) -> str:
        length = len(self.msg)
        key = ""
        for _ in range(length):
            a = secrets.choice(range(65, 91))
            key += chr(a)
        return key

    def encrypt_word(self) -> tuple[str, str]:
        key = self.generate_key()
        iterable_key = iter(
            key
        )  # Making the key iterable so as to use the next function to encrypt
        iterable_msg = iter(self.msg)
        encrypted_msg = ""
        while True:
            try:
                current_key = next(iterable_key)
                current_msg = next(iterable_msg)
                key_char = ord(current_key) - 65
                msg_char = ord(current_msg) - 65
                encrypted_char = ((key_char + msg_char) % 26) + 65
                encrypted_msg += chr(encrypted_char)
            except:
                break
        return encrypted_msg, key

    def decrypt_word(self, encrypted_msg, key) -> str:
        decrypted_msg = ""
        iterable_encrypted_msg = iter(encrypted_msg)
        iterable_key = iter(key)
        while True:
            try:
                current_key = next(iterable_key)
                current_msg = next(iterable_encrypted_msg)
                key_char = ord(current_key) - 65
                msg_char = ord(current_msg) - 65
                decrypted_val = msg_char - key_char
                if decrypted_val >= 0:
                    decrypted_val %= 26
                else:
                    decrypted_val = 26 + decrypted_val
                decrypted_char = chr(decrypted_val + 65)
                decrypted_msg += decrypted_char
            except:
                break
        return decrypted_msg
