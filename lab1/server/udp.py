import socket

employees = {
    "john": "manager",
    "jane": "steno",
    "jim": "clerk",
    "jack": "salesman"
}


def start_udp_server(host='127.0.0.1', port=13000):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    print(f"[+] UDP-сервер запущен на {host}:{port}")

    while True:
        data, addr = server.recvfrom(1024)
        name = data.decode().strip().lower()
        print(f"[>] Получено '{name}' от {addr}")

        job = employees.get(name, "No such employee")
        server.sendto(job.encode(), addr)


if __name__ == "__main__":
    start_udp_server()
