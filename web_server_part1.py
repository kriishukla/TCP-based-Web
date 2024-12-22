from socket import *
import sys

# Create a socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to an address and port
serverSocket.bind(('', 6789))

# Set the server to listen for incoming connections
serverSocket.listen(1)

print('Ready to serve...')

while True:
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        # Open the file requested by the client
        f = open(filename[1:])
        outputdata = f.read()

        # Send HTTP header
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        
        # Send the contents of the file
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())

        # Close the connection
        connectionSocket.close()

    except IOError:
        # Send 404 Not Found response
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("404 Not Found".encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()
