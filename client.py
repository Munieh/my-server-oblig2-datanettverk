import argparse
import socket

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="HTTP client")
    parser.add_argument("-i", "--server_ip", help="Server IP address", required=True)
    parser.add_argument("-p", "--server_port", help="Server port number", type=int, required=True)
    parser.add_argument("-f", "--filename", help="File path at the server", required=True)
    args = parser.parse_args()

    # Extract arguments
    server_host = args.server_ip
    server_port = args.server_port
    filename = args.filename

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Try connecting to the server
    try:
        client_socket.connect((server_host, server_port))
        print(f"Connected to server at {server_host}:{server_port}")

        # Send an HTTP GET request to the server
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}:{server_port}\r\n\r\n"
        client_socket.sendall(request.encode())

        # Receive the response from the server
        response = client_socket.recv(1024).decode()
        print(response)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    main()
