import string
ALPHABET = string.ascii_lowercase

def encrypt(message, key):
    chiffre = ""
    while len(key) < len(message):
        key = key + key
    for i, (message_index, key_index) in enumerate(zip(message, key)):
        key_number = ALPHABET.index(key_index)
        message_number = ALPHABET.index(message_index)
        chiffre_number = (key_number + message_number) % len(ALPHABET)
        chiffre = chiffre + ALPHABET[chiffre_number]
    return chiffre
    

def decrypt(chiffre, key):
    message = ""
    while len(key) < len(chiffre):
        key = key + key
    for i, (chiffre_index, key_index) in enumerate(zip(chiffre, key)):
        key_number = ALPHABET.index(key_index)
        chiffre_number = ALPHABET.index(chiffre_index)
        message_number = chiffre_number - key_number
        if message_number < 0:
            message_number += len(ALPHABET)
        message = message + ALPHABET[message_number]
    return message

if __name__ == "__main__":
    mode = input("Modus e oder d: ").lower()
    if mode == "e":
        message = input("Message: ").lower()
        key = input("Passkey: ").lower()
        print(encrypt(message, key))
    elif mode == "d":
        chiffre = input("Chiffre: ").lower()
        key = input("Passkey: ").lower()
        print(decrypt(chiffre, key))
    else:
        exit(1)
