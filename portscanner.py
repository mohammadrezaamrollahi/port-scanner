import socket

target_ip = input("Enter the target IP address: ")

start_port = int(input("Enter the start port number: "))
end_port = int(input("Enter the end port number: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for port in range(start_port, end_port+1):
    try:
        sock.connect((target_ip, port))
        print(f"Port {port} is open")
    except:
        print(f"Port {port} is closed")

sock.close()
