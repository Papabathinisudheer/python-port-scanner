import socket
from datetime import datetime


def scan_ports(host, start_port, end_port):
    print("\n===== PYTHON PORT SCANNER =====")
    print("Target:", host)
    print("Scan started:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Resolve hostname into an IP address
    try:
        ip_address = socket.gethostbyname(host)
        print("IP Address:", ip_address)
    except socket.gaierror:
        print("Error: Hostname could not be resolved.")
        return

    print("-" * 40)
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        try:
            result = sock.connect_ex((ip_address, port))

            if result == 0:
                print(f"Port {port}: OPEN")
                open_ports.append(port)

        except OSError:
            pass

        finally:
            sock.close()

    print("-" * 40)
    print("Total open ports found:", len(open_ports))

    if open_ports:
        print("Open ports:", ", ".join(map(str, open_ports)))
    else:
        print("No open ports found in the selected range.")

    print("Scan completed:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    print("Authorized systems only.")
    host = input("Enter target hostname or IP: ").strip()

    try:
        start_port = int(input("Enter starting port (1-65535): "))
        end_port = int(input("Enter ending port (1-65535): "))

        if not host:
            print("Error: Target cannot be empty.")
        elif not (1 <= start_port <= end_port <= 65535):
            print("Error: Invalid port range.")
        elif end_port - start_port > 999:
            print("Error: Scan a maximum of 1000 ports per run.")
        else:
            scan_ports(host, start_port, end_port)

    except ValueError:
        print("Error: Please enter valid integer port numbers.")
