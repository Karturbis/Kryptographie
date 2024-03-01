"""This module encrypts and decrypts messages
using the vigenère method."""
import string
ALPHABET = string.ascii_uppercase
TOSTRIP = "!§$%&/()=?`´+#*,.-_;:'\" äüö"

def encrypt(message, key):
    """This method encrypts a given message with
    a given key. It returns the chiffre."""
    chiffre = ""
    while len(key) < len(message):
        key = key + key
    print(f"\nLOG: The key is now: {key}")
    for i, (message_index, key_index) in enumerate(zip(message, key)):
        if TOSTRIP.find(message_index) != -1:
            chiffre = chiffre + message_index
            print(f"\nLOG: the character '{message_index}' is a special character, it will not be encrypted.")
            continue
        key_number = ALPHABET.index(key_index)
        print(f"\nLOG character {i+1}: The key letter ({key_index}) has the number {key_number}.")
        message_number = ALPHABET.index(message_index)
        print(f"LOG character {i+1}: The message letter ({message_index}) has the number {message_number}.")
        chiffre_number = (key_number + message_number) % len(ALPHABET)
        print(f"LOG character {i+1}: The chiffre number ({key_number} + {message_number} = {key_number + message_number}) % {len(ALPHABET)} = {chiffre_number}.")
        chiffre = chiffre + ALPHABET[chiffre_number]
        print(f"LOG character {i+1}: The chiffre number ({chiffre_number}) gets converted to '{ALPHABET[chiffre_number]}'.")
        print(f"LOG character {i+1}: The chiffre is now: '{chiffre}'")
    return chiffre


def decrypt(chiffre, key):
    """This method decrypts a given chiffre with
    the given key. It returns the message."""
    message = ""
    while len(key) < len(chiffre):
        key = key + key
        print(f"\nLOG: The key is now: {key}")
    for i, (chiffre_index, key_index) in enumerate(zip(chiffre, key)):
        if TOSTRIP.find(chiffre_index) != -1:
            message = message + chiffre_index
            print(f"\nLOG: the character '{chiffre_index}' is a special character, it will not be decrypted.")
            continue
        key_number = ALPHABET.index(key_index)
        print(f"\nLOG character {i+1}: The key letter ({key_index}) has the number {key_number}.")
        chiffre_number = ALPHABET.index(chiffre_index)
        print(f"LOG character {i+1}: The chiffre letter ({chiffre_index}) has the number {chiffre_number}.")
        message_number = chiffre_number - key_number
        if message_number < 0:
            message_number += len(ALPHABET)
            print(f"LOG character {i+1}: The message number ({chiffre_number} - {key_number} = {chiffre_number - key_number}) + {len(ALPHABET)} = {message_number}.")
        else:
            print(f"LOG character {i+1}: The message number ({chiffre_number} - {key_number}) = {message_number}.")
        message = message + ALPHABET[message_number]
        print(f"LOG character {i+1}: The message number ({message_number}) gets converted to '{ALPHABET[message_number]}'")
        print(f"LOG character {i+1}: The message is now: '{message}'")
    return message

if __name__ == "__main__":
    print("Please run main.py to execute this file!")
