import socket


def start_udp_client(server_host='127.0.0.1', server_port=13000):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        name = input("Имя: ")
        if not name:
            break

        client.sendto(name.encode(), (server_host, server_port))
        data, _ = client.recvfrom(1024)
        print(data.decode())

    client.close()


if __name__ == "__main__":
    start_udp_client()
