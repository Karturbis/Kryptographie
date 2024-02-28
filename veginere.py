"""This module encrypts and decrypts messages
using the veginere method."""
import string
ALPHABET = string.ascii_lowercase
TOSTRIP = "!§$%&/()=?`´+#*,.-_;:'\" äüö"

def encrypt(message, key):
    """This method encrypts a given message with
    a given key. It returns the chiffre."""
    chiffre = ""
    while len(key) < len(message):
        key = key + key
    for i, (message_index, key_index) in enumerate(zip(message, key)):
        if TOSTRIP.find(message_index) != -1:
            chiffre = chiffre + message_index
            continue
        key_number = ALPHABET.index(key_index)
        message_number = ALPHABET.index(message_index)
        chiffre_number = (key_number + message_number) % len(ALPHABET)
        chiffre = chiffre + ALPHABET[chiffre_number]
    return chiffre


def decrypt(chiffre, key):
    """This method decrypts a given chiffre with
    the given key. It returns the message."""
    message = ""
    while len(key) < len(chiffre):
        key = key + key
    for i, (chiffre_index, key_index) in enumerate(zip(chiffre, key)):
        if TOSTRIP.find(chiffre_index) != -1:
            message = message + chiffre_index
            continue
        key_number = ALPHABET.index(key_index)
        chiffre_number = ALPHABET.index(chiffre_index)
        message_number = chiffre_number - key_number
        if message_number < 0:
            message_number += len(ALPHABET)
        message = message + ALPHABET[message_number]
    return message

if __name__ == "__main__":
    print("Please run main.py to execute this file!")
