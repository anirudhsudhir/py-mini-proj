import secrets
class Vignere:
    def __init__(self,msg):
        self.msg = msg              # Message to be encrypted or decrypted

    def generate_key(self):
        length = len(self.msg)
        key = ""
        for _ in range(length):
            a = secrets.choice(range(65,91))
            key+=chr(a)
        return key
    
    def encrypt(self):
        key = self.generate_key()
        iterable_key = iter(key)        # Making the key iterable so as to use the next function to encrypt
        iterable_msg = iter(self.msg)
        encrypted_msg = ""
        while True:
            try:
                a = next(iterable_key)
                b = next(iterable_msg)
                encrypted_msg+=chr(ord(a)+ord(b))
            except BaseException:
                break
        print("The key used to encrypt is:",key)
        print("-"*50)
        print("The encrypted message is:")
        return encrypted_msg,key
    
    def decrypt(self,encrypted_msg,key):
        decrypted_msg = ""
        iterable_encrypted_msg = iter(encrypted_msg)
        iterable_key = iter(key)
        while True:
            try:
                a = next(iterable_encrypted_msg)
                b = next(iterable_key)
                decrypted_msg+=chr(ord(a)-ord(b))
            except BaseException:
                break
        print("Decrypted message is:")
        return decrypted_msg
sample = "This is a demo for the python mini project"

test1 = Vignere(sample)
a = test1.encrypt()
print("Encrypted message is:",a[0])
print("-"*50)
print(test1.decrypt(a[0],a[1]))

