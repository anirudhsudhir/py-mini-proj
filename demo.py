import secrets


class Vignere:
    def __init__(self, msg):
        self.msg = msg.upper()  # Message to be encrypted or decrypted
        print(self.msg)

    def generate_key(self):
        length = len(self.msg)
        key = ""
        for _ in range(length):
            a = secrets.choice(range(65, 91))
            key += chr(a)
        return key

    def encrypt(self):
        key = self.generate_key()
        # key = "JCHX"
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
        print("The key used to encrypt is:", key)
        print("-" * 50)
        print("The encrypted message is:", encrypted_msg)
        return encrypted_msg, key

    def decrypt(self, encrypted_msg, key):
        decrypted_msg = ""
        print("Encrypted Message being used is ", encrypted_msg)
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
                print(
                    current_key,
                    current_msg,
                    key_char,
                    msg_char,
                    decrypted_val,
                    decrypted_char,
                )
                decrypted_msg += decrypted_char
            except:
                break
        print("Decrypted message is:")
        return decrypted_msg


# sample = "This is a demo for the python mini project"
sample = "FANZEZ"

test1 = Vignere(sample)
encrypted_message, encryption_key = test1.encrypt()
print("Encrypted message is:", encrypted_message)
print("-" * 50)
print(test1.decrypt(encrypted_message, encryption_key))
