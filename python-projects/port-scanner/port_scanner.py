import socket

target = input("Enter IP address: ")

print(f"\nScanning {target}...\n")

for port in range [21,22,23,25,53,80,110,143,443]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(0.1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()

print("\nScan Complete!")
