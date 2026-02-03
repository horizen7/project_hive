from socket import *

### socket set ###
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

### End/Dec ###
ALPHABET_SIZE = 128  # ASCII 0–127

def vigenere_encrypt(plaintext: str, key: str) -> str:
    result_chars = []
    key_len = len(key)
    for i, ch in enumerate(plaintext):
        p = ord(ch)
        k = ord(key[i % key_len])
        c = (p + k) % ALPHABET_SIZE
        result_chars.append(chr(c))
    return "".join(result_chars)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    result_chars = []
    key_len = len(key)
    for i, ch in enumerate(ciphertext):
        c = ord(ch)
        k = ord(key[i % key_len])
        p = (c - k) % ALPHABET_SIZE
        result_chars.append(chr(p))
    return "".join(result_chars)

### ready ###
print("The server is ready to receive")

### new key needed every iteration
k, clientAddress = serverSocket.recvfrom(2048)
key = k.decode()
ACK = "Acknowledged"
serverSocket.sendto(ACK.encode(), clientAddress)

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    cipherText = message.decode()
    plainText = vigenere_decrypt(cipherText, key)
    if plainText == "Bye":
        response = vigenere_encrypt("Goodbye.", key)
        serverSocket.sendto(response.encode(), clientAddress)
        break
    print(f"Encrypted message: {cipherText}\nDecrypted message: {plainText}\nSending back encoded...")

    #now sending back
    response = vigenere_encrypt(plainText, key)
    serverSocket.sendto(response.encode(), clientAddress)
    print("Sent!\n")

