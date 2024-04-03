from socket import *
import os.path


def handle_request(client_socket):

    # Recives the client request and decodes it
    request = client_socket.recv(1024).decode()

    # Parses the HTTP request message to get the requested file path
    file_path = request.split()[1][1:]

    # If-test to check if the parameter "file_path" is on the server
    if os.path.exists(file_path):
        # If the file exists, open the file as f
        with open(file_path, "rb") as f:
            file_contents = f.read()    # Then read the file

        # Creat an HTTP response message consisting of the requested file preceded by header lines
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += f"Content-Length: {len(file_contents)}\r\n"
        response += "\r\n"

        # Last to encode and ads file content
        response = response.encode()

        # Add the file contents to the response
        response += file_contents

    else:
        # If the file does not exist, creat an HTTP response message with a 404 status code and a message
        # indicating that the requested file was not found
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type: text/plain\r\n"
        response += "\r\n"
        response += "404 Not Found: The requested file was not found on this server."

        response = response.encode()   # Encode the file as binary

    # Send the HTTP response message back to the client
    client_socket.sendall(response)

    # Close the connection
    client_socket.close()

# Main function
def main():
    # Create a server socket
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(('', 8000))
    serverSocket.listen(1)

    while True:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        handle_request(connectionSocket)

if __name__ == "__main__":
    main()