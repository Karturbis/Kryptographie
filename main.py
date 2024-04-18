"""This is the main module of the Kryptographie
project, it is used to handle the requests to the
different encryption algorythms."""
import vigenere

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
    input_str = input_str.replace("Ä", "AE")
    input_str = input_str.replace("Ö", "OE")
    input_str = input_str.replace("Ü", "UE")
    print("LOG: removed special characters from string.")
    return input_str

if __name__ == "__main__":
    strip_mode = "s"#input("Secure or unsecure? [S/u]: ").lower()
    mode = input("Modus Encryption (e) oder Decryption (d): ").lower()
    if mode == "e":
        print("Encryption mode is enabled.")
        message = input("Message: ").upper()
        if strip_mode == "u":
            pass
        else:
            message = input_strip(message)
        key = input_strip(input("Passkey: ").upper())
        print("\nThe chiffre is:\n" + vigenere.encrypt(message, key))

    elif mode == "d":
        print("Decryption mode is enabled.")
        chiffre = input("Chiffre: ").upper()
        key = input_strip(input("Passkey: ").upper())
        print("\nThe message is:\n" + vigenere.decrypt(chiffre, key))
    else:
        exit(0)
