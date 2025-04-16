import socket


def start_client(server_host='127.0.0.1', server_port=14001):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    print("Вводите строки текста. Пустая строка завершает работу.")
    while True:
        line = input("> ").strip()
        if line == "":
            break

        client.sendall((line + "\n").encode())
        response = client.recv(4096).decode()
        print("Ответ сервера:")
        print(response.strip())

    client.close()


if __name__ == "__main__":
    start_client()
