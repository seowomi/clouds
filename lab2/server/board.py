import socket
import threading

ADS_FILE = "ads.txt"


def handle_client(conn, addr):
    print(f"[+] Подключение от {addr}")
    try:
        while True:
            data = conn.recv(1024).decode().strip()
            if not data:
                break

            if data.upper() == "LIST":
                try:
                    with open(ADS_FILE, 'r') as f:
                        ads = f.read()
                except FileNotFoundError:
                    ads = "[!] Нет объявлений."
                conn.sendall((ads + "\n").encode())
            else:
                with open(ADS_FILE, 'a') as f:
                    f.write(data + "\n")
                conn.sendall(f'Сообщение добавлено: "{data}"\n'.encode())
    except Exception as e:
        print(f"[!] Ошибка: {e}")
    finally:
        conn.close()
        print(f"[-] Отключение от {addr}")


def start_server(host='127.0.0.1', port=15000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[✓] Сервер «Доска объявлений» слушает на {host}:{port}")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    start_server()
