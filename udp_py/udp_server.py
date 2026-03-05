from socket import *

### socket set ###
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Server ready.")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(f'Received message: {message.decode()}')