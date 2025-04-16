import socket
import threading

employees = {
    "john": "manager",
    "jane": "steno",
    "jim": "clerk",
    "jack": "salesman"
}


def handle_client(client_socket, address):
    print(f"[+] Подключен клиент: {address}")
    client_socket.sendall(f"{len(employees)} Employees available\n".encode())

    while True:
        data = client_socket.recv(1024).decode().strip()
        if not data:
            break
        job = employees.get(data.lower(), "No such employee")
        client_socket.sendall((job + "\n").encode())

    print(f"[-] Отключен клиент: {address}")
    client_socket.close()


def start_server(host='127.0.0.1', port=13000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[+] Сервер слушает на {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()


if __name__ == "__main__":
    start_server()
