import subprocess

def run_osint(target):
    print(f"[+] Performing WHOIS lookup for {target}...")
    whois_result = subprocess.getoutput(f"whois {target}")

    print(f"[+] Performing DNS lookup...")
    dig_result = subprocess.getoutput(f"dig {target}")

    result = f"WHOIS Info:\n{whois_result}\n\nDNS Info:\n{dig_result}"
    print(result)
    return result
