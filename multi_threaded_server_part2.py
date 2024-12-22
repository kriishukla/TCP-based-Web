from socket import *
import sys
import threading

def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        if not message:  # Check if the message is empty (client disconnected)
            return
        
        filename = message.split()[1]
        try:
            with open(filename[1:], 'r') as f:  # Open the requested file
                outputdata = f.read()
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            connectionSocket.send(outputdata.encode())
        except IOError:
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("404 Not Found".encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connectionSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 6789))
serverSocket.listen(5)

print('Ready to serve...')

while True:
    connectionSocket, addr = serverSocket.accept()
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
    client_thread.start()

serverSocket.close()
sys.exit()
