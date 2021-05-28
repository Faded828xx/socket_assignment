from socket import *
serverPort = 13000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
while True:
    connectionSocket, address = serverSocket.accept()
    message = connectionSocket.recv(1024)
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage)
    connectionSocket.close()