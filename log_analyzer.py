import re
from collections import Counter

def analyze_logs(log_file_path):
    """Analyzes a web server log file and prints a summary report."""
    ip_addresses = []
    requested_pages = []
    error_404_count = 0

    # Regex pattern to extract IP, Requested URL, and HTTP Status Code
    log_pattern = re.compile(r'^(?P<ip>\S+) .*?"[A-Z]+ (?P<url>\S+) HTTP/\d\.\d" (?P<status>\d{3})')

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = log_pattern.search(line)
                if match:
                    # Extract the data using the regex groups
                    ip = match.group('ip')
                    url = match.group('url')
                    status = match.group('status')

                    ip_addresses.append(ip)
                    requested_pages.append(url)
                    
                    if status == '404':
                        error_404_count += 1

        # Calculate the top 3 results
        top_ips = Counter(ip_addresses).most_common(3)
        top_pages = Counter(requested_pages).most_common(3)

        # Print the final formatted report
        print("=== Web Server Log Analysis Report ===")
        print(f"Total 404 Errors Found: {error_404_count}\n")
        
        print("Top 3 IP Addresses:")
        for ip, count in top_ips:
            print(f" - {ip} ({count} requests)")
            
        print("\nTop 3 Requested Pages:")
        for page, count in top_pages:
            print(f" - {page} ({count} requests)")

    except FileNotFoundError:
        print(f"Error: The log file '{log_file_path}' could not be found.")

if _name_ == "_main_":
    # Create a dummy server log file to demonstrate functionality
    dummy_logs = """
192.168.1.10 - - [31/May/2026:20:00:00 +0000] "GET /home HTTP/1.1" 200 512
10.0.0.5 - - [31/May/2026:20:01:00 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.10 - - [31/May/2026:20:02:00 +0000] "GET /missing-page HTTP/1.1" 404 128
192.168.1.10 - - [31/May/2026:20:03:00 +0000] "GET /home HTTP/1.1" 200 512
172.16.0.2 - - [31/May/2026:20:04:00 +0000] "GET /dashboard HTTP/1.1" 404 128
10.0.0.5 - - [31/May/2026:20:05:00 +0000] "GET /home HTTP/1.1" 200 512
192.168.1.10 - - [31/May/2026:20:06:00 +0000] "GET /admin HTTP/1.1" 403 128
    """
    with open("server_logs.txt", "w") as f:
        f.write(dummy_logs.strip())
        
    # Run the analyzer on the newly created file
    analyze_logs("server_logs.txt")