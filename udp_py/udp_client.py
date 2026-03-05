from socket import *

### set socket ###
serverName = '10.244.88.131'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

## for json, dump and load
message = "hello"
clientSocket.sendto(message.encode(), (serverName, serverPort))
print("sent.\n")
clientSocket.close()