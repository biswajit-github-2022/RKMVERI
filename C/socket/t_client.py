import socket

def start_client():
    # Set up the client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))

    # Send data to the server
    client.send(b"Hello, server!")

    # Receive the response from the server
    response = client.recv(1024)
    print(f"[*] Received: {response.decode('utf-8')}")

    # Close the client socket
    client.close()

if __name__ == "__main__":
    start_client()
