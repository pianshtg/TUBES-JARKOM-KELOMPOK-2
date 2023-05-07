import socket

# Fungsi untuk mencari dan membaca file yang diminta oleh client
def read_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return None

# Fungsi untuk memparsing HTTP request dari client
def parse_http_request(request):
    lines = request.split('\r\n')
    if len(lines) > 0:
        method, path, _ = lines[0].split(' ')
        return method, path
    return None, None

# Inisialisasi alamat IP dan port server
HOST = 'localhost'
PORT = 8080

# Pembuatan TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket ke alamat IP dan port tertentu
server_socket.bind((HOST, PORT))

# Listen permintaan koneksi dari client
server_socket.listen(1)
print('Web server berjalan pada {}:{}'.format(HOST, PORT))

while True:
    # Terima koneksi baru
    client_socket, addr = server_socket.accept()
    print('Terhubung dengan client:', addr)

    # Terima data dari client
    request_data = client_socket.recv(1024).decode('utf-8')
    print('HTTP request dari client:\n', request_data)

    # Parse HTTP request
    method, path = parse_http_request(request_data)

    # Tutup koneksi dengan client
    client_socket.close()