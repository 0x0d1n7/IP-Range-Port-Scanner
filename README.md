**IP Range Port Scanner**

This Python script allows you to scan for open ports within a specified IP range or on a single IP address. It utilizes the socket module to establish TCP connections and checks for open ports on each IP address in the given range or the specified IP.

Features

    Scans for open ports within a specified IP range or on a single IP address
    Supports scanning for standard ports (e.g., SSH, HTTP, HTTPS, RDP)
    Scans for ports between 1 and 1000
    Provides a simple and straightforward command-line interface

Prerequisites

    Python 3

Usage

    Clone the repository and navigate to the project directory.
    Run the script using Python 3:

python3 port_scanner.py

    Follow the prompts to enter the network interface and the IP range or IP address to scan.
    The script will scan for open ports on each IP address in the specified range or the provided IP and display the results.
    
Disclaimer

This script is intended for educational and ethical purposes only. Please ensure that you have proper authorization to perform port scanning on the target IP range or IP address. Be mindful of the potential impact on network performance and security. It is your responsibility to comply with all applicable laws and regulations.

License

This project is licensed under the MIT License.
