def is_public_ip(ip_address):
    # Define the private IP address ranges
    private_ranges = [
        ('10.0.0.0', '10.255.255.255'),
        ('172.16.0.0', '172.31.255.255'),
        ('192.168.0.0', '192.168.255.255')
    ]

    # Convert the IP address to an integer for comparison
    def ip_to_int(ip):
        parts = ip.split('.')
        return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])

    # Convert the given IP address to an integer
    ip_int = ip_to_int(ip_address)

    # Check if the IP address is within the private ranges
    for start, end in private_ranges:
        if ip_int >= ip_to_int(start) and ip_int <= ip_to_int(end):
            return False  # It's a private IP address

    return True  # It's a public IP address


# Example usage
ip = '203.0.113.100'
if is_public_ip(ip):
    print(f"{ip} is a public IP address.")
else:
    print(f"{ip} is a private IP address.")
