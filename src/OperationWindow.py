from tkinter import *

import Tokenize


def createEncryptionWindow():
    def disp_encrypt():
        text_to_encrypt = message_text.get(1.0, "end-1c")
        encrypted_text, encryption_key = Tokenize.encrypt_message(text_to_encrypt)
        message_text.destroy()
        encrypt_button.destroy()
        message_text_label.destroy()
        encrypted_text_label = Label(EncryptWindow, text="Encrypted Text")
        encrypted_text_label.pack()
        encrypted_text = Label(EncryptWindow, text=encrypted_text)
        encrypted_text.pack()
        encryption_key_label = Label(EncryptWindow, text="Encryption Key")
        encryption_key_label.pack()
        encryption_key_text = Label(EncryptWindow, text=encryption_key)
        encryption_key_text.pack()

    EncryptWindow = Tk()
    message_text = Text()
    encrypt_button = Button(text="Encrypt Text", command=disp_encrypt)
    message_text_label = Label(EncryptWindow, text="Enter the plaintext")
    message_text_label.pack()
    message_text.pack()
    encrypt_button.pack()
    EncryptWindow.mainloop()


def createDecryptionWindow():
    def disp_decrypt():
        encrypted_text_label.destroy()
        encrypted_textbox.destroy()
        encryption_key_label.destroy()
        encryption_key_textbox.destroy()
        decrypt_button.destroy()
        message_text = Text()
        message_text_label = Label(EncryptWindow, text="Plaintext")
        message_text_label.pack()
        message_text.pack()

    EncryptWindow = Tk()
    encrypted_text_label = Label(EncryptWindow, text="Encrypted Text")
    encrypted_text_label.pack()
    encrypted_textbox = Text()
    encrypted_textbox.pack()
    encryption_key_label = Label(EncryptWindow, text="Encryption Key")
    encryption_key_label.pack()
    encryption_key_textbox = Text()
    encryption_key_textbox.pack()
    decrypt_button = Button(text="Decrypt Text", command=disp_decrypt)
    decrypt_button.pack()
    EncryptWindow.mainloop()
