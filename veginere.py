import string
ALPHABET = string.ascii_lowercase

def input_strip(message):
    input_str = input(message).lower()
    for i in "!§$%&/()=?`´+#* ":
        input_str = input_str.replace(i, "")
    input_str = input_str.replace("ä", "ae")
    input_str = input_str.replace("ö", "oe")
    input_str = input_str.replace("ü", "ue")
    input_str = input_str.replace("ß", "ss")
    return input_str

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
    mode = input_strip("Modus e oder d: ")
    if mode == "e":
        message = input_strip("Message: ")
        key = input_strip("Passkey: ")
        print(encrypt(message, key))

    elif mode == "d":
        chiffre = input_strip("Chiffre: ")
        key = input_strip("Passkey: ")
        print(decrypt(chiffre, key))
    else:
        exit(0)
