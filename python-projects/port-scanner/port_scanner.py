import socket

target = input("Enter IP address or hostname: ")

ip = socket.gethostbyname(target)

print(f"Hostname: {target}")
print(f"IP Address: {ip}")
print(f"\nScanning {ip}...\n")

for port in [22, 80, 443]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    s.close()

print("\nScan Complete!")
