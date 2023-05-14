import socket

# Function to check if a port is open
def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set the timeout for the connection attempt
    result = sock.connect_ex((ip, port))
    sock.close()
    if result == 0:
        print(f"Port {port} is open on {ip}")
        determine_device_type(port)

# Function to determine device type based on open port
def determine_device_type(port):
    port_mappings = {
        22: "SSH (Secure Shell)",
        80: "HTTP (Hypertext Transfer Protocol)",
        443: "HTTPS (Hypertext Transfer Protocol Secure)",
        3389: "RDP (Remote Desktop Protocol)",
        # Add more port-to-service mappings here
    }
    if port in port_mappings:
        print(f"Potential device type: {port_mappings[port]}")
    else:
        print("No device type mapping available for this port")

# Read user input for interface and IP(s)
interface = input("Enter the network interface to scan (e.g., eth0): ")
target = input("Enter the IP address or range to scan (e.g., 192.168.0.1 or 192.168.0.1-192.168.0.10): ")

# Check if the target is a single IP or a range
if '-' in target:
    start_ip, end_ip = target.split('-')

    # Extracting the first three octets of the start IP
    base_ip = '.'.join(start_ip.split('.')[:3])

    # Loop through the IP range and scan for ports
    for ip in range(int(start_ip.split('.')[-1]), int(end_ip.split('.')[-1]) + 1):
        ip_address = f"{base_ip}.{ip}"
        print(f"Scanning ports on {ip_address}...")

        # Port scanning for standard ports
        check_port(ip_address, 22)  # SSH
        check_port(ip_address, 80)  # HTTP
        check_port(ip_address, 443)  # HTTPS
        check_port(ip_address, 3389)  # RDP

        print(f"Scan complete for {ip_address}")
        print()
else:
    # Single IP address
    ip_address = target
    print(f"Scanning ports on {ip_address}...")

    # Port scanning for standard ports
    check_port(ip_address, 22)  # SSH
    check_port(ip_address, 80)  # HTTP
    check_port(ip_address, 443)  # HTTPS
    check_port(ip_address, 3389)  # RDP

    print(f"Scan complete for {ip_address}")
    print()
