"""This is the main module of the Kryptographie
project, it is used to handle the requests to the
different encryption algorythms."""
import veginere

TOSTRIP = "!§$%&/()=?`´+#*,.-_;:'\" "

def input_strip(message):
    """This method takes a string and
    removes every character from it,
    that is found in the TOSTRIP string.
    Further it changes some letters to
    ASCII valid combinations of letters."""
    input_str = message
    for i in TOSTRIP:
        input_str = input_str.replace(i, "")
    input_str = input_str.replace("ä", "ae")
    input_str = input_str.replace("ö", "oe")
    input_str = input_str.replace("ü", "ue")
    input_str = input_str.replace("ß", "ss")
    return input_str

if __name__ == "__main__":
    strip_mode = input("Secure or unsecure? [S/u]: ").lower()
    mode = input_strip(input("Modus e oder d: "))
    if mode == "e":
        message = input("Message: ").lower()
        if strip_mode == "u":
            pass
        else:
            message = input_strip(message)
        key = input_strip(input("Passkey: ").lower())
        print(veginere.encrypt(message, key))

    elif mode == "d":
        chiffre = input("Chiffre: ").lower()
        key = input_strip(input("Passkey: ").lower())
        print(veginere.decrypt(chiffre, key))
    else:
        exit(0)
