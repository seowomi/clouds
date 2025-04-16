import socket


def start_client(server_host='127.0.0.1', server_port=15000):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    print("Введите сообщение (или LIST для просмотра, пустая строка — выход):")
    while True:
        message = input("> ").strip()
        if message == "":
            break

        client.sendall((message + "\n").encode())
        response = client.recv(4096).decode()
        print(response.strip())

    client.close()


if __name__ == "__main__":
    start_client()
