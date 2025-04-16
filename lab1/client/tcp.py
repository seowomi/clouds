import socket


def start_client(host='127.0.0.1', port=13000):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print(client.recv(1024).decode())

    while True:
        name = input("Имя: ")
        if not name:
            break
        client.sendall((name + "\n").encode())
        print(client.recv(1024).decode())

    client.close()


if __name__ == "__main__":
    start_client()
