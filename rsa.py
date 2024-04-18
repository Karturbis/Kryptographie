d = 173
e = 5
p = 17
q = 19
N = p*q

message = 24

def encrypt(N, e, message):
    chiffre = (message**e) % N
    return chiffre

def decrypt(N, d, chiffre):
    message = (chiffre**d) % N
    return message

chiffre = encrypt(N, e, message)
print(f"Das Chiffre ist: {chiffre}")
message = decrypt(N, d, chiffre)
print(f"Die Nachricht ist: {message}")
