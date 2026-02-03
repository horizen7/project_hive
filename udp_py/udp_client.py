from socket import *

### set socket ###
serverName = '192.168.29.2'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

### Encryption/Decryption code ###
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

### sending to server ###
k = input('input key: ')
clientSocket.sendto(k.encode(), (serverName, serverPort))
ACK, serverAddress = clientSocket.recvfrom(2048)
print(ACK.decode())

while True:
    #sending
    message = input('input message: ')
    clientSocket.sendto((vigenere_encrypt(message, k)).encode(), (serverName, serverPort))

    #receiving
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    decodedMessage = vigenere_decrypt(modifiedMessage.decode(), k)
    if decodedMessage == "Goodbye.":
        print(decodedMessage)
        break
    print(f"Encrypted: {modifiedMessage} Decrypted: {decodedMessage}")

clientSocket.close()