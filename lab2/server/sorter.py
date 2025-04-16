import socket
import threading


def process_text(text):
    words = set(text.lower().split())
    return '\n'.join(sorted(words))


def handle_client(conn, addr):
    print(f"[+] Подключен клиент: {addr}")
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            sorted_words = process_text(data)
            conn.sendall((sorted_words + '\n').encode())
    except Exception as e:
        print(f"[!] Ошибка: {e}")
    finally:
        conn.close()
        print(f"[-] Отключение клиента: {addr}")


def start_server(host='127.0.0.1', port=14001):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[✓] Сервер «Сортировщик слов» слушает на {host}:{port}")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    start_server()
