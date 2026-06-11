import socket

target = input("Enter IP address: ")

print(f"\nScanning {target}...\n")

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()

print("\nScan Complete!")
