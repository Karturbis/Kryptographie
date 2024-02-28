import veginere

TOSTRIP = "!§$%&/()=?`´+#*,.-_;:'\" "

def input_strip(message):
    input_str = input(message).lower()
    for i in TOSTRIP:
        input_str = input_str.replace(i, "")
    input_str = input_str.replace("ä", "ae")
    input_str = input_str.replace("ö", "oe")
    input_str = input_str.replace("ü", "ue")
    input_str = input_str.replace("ß", "ss")
    return input_str

if __name__ == "__main__":
    mode = input_strip("Modus e oder d: ")
    if mode == "e":
        message = input_strip("Message: ")
        key = input_strip("Passkey: ")
        print(veginere.encrypt(message, key))

    elif mode == "d":
        chiffre = input_strip("Chiffre: ")
        key = input_strip("Passkey: ")
        print(veginere.decrypt(chiffre, key))
    else:
        exit(0)