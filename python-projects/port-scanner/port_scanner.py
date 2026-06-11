import socket

target = input("Enter IP address or hostname: ")

ip = socket.gethostbyname(target)

start_port = intc(input("enter start port: "))
end_port = int(input("enter end port: "))

print(f"Hostname: {target}")
print(f"IP Address: {ip}")
print(f"\nScanning ports {start_port} to {end_port)...\n")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    s.close()

print("\nScan Complete!")
