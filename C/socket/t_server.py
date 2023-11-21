import socket
import threading

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break  # If no data is received, break the loop

        # Send the received data back to the client
        client_socket.send(data)

    # Close the client socket when the loop breaks
    client_socket.close()

def start_server():
    # Set up the server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8888))
    server.listen(5)  # Allow up to 5 queued connections

    print("[*] Listening on 127.0.0.1:8888")

    while True:
        # Accept a client connection
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
