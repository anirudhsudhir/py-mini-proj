import tkinter as tk

import OperationWindow


def createEncryptionWindow():
    mainWindow.destroy()
    OperationWindow.createEncryptionWindow()


def createDecryptionWindow():
    mainWindow.destroy()
    OperationWindow.createDecryptionWindow()


mainWindow = tk.Tk()
mainWindow.geometry("1000x1000")
mainWindow.attributes("-alpha", 0.7)

# Encrypt Button
encrypt_button = tk.Button(mainWindow, text="Encrypt", command=createEncryptionWindow)
encrypt_button.pack()

# Decrypt Button
decrypt_button = tk.Button(mainWindow, text="Decrypt", command=createDecryptionWindow)
decrypt_button.pack()

mainWindow.mainloop()
