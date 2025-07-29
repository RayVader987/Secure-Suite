import subprocess

def run_nmap(target):
    print(f"[+] Scanning target {target} using Nmap...")
    result = subprocess.getoutput(f"nmap -sV -T4 {target}")
    print(result)
    return result
