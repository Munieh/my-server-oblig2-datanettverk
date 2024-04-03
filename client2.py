import argparse
import socket
import threading

def send_request(server_ip, server_port, filename):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))

        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_ip}:{server_port}\r\n\r\n"
        client_socket.sendall(request.encode())

        response = client_socket.recv(1024).decode()
        print(response)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

def main():
    parser = argparse.ArgumentParser(description="HTTP client")
    parser.add_argument("-i", "--server_ip", help="Server IP address", required=True)
    parser.add_argument("-p", "--server_port", help="Server port number", type=int, required=True)
    parser.add_argument("-f", "--filename", help="File path at the server", required=True)
    args = parser.parse_args()

    # Start threads to send requests concurrently
    threads = []
    for _ in range(5):  # Example: sending 5 requests concurrently
        thread = threading.Thread(target=send_request, args=(args.server_ip, args.server_port, args.filename))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
