import requests

def scan_web(target):
    print(f"[+] Checking for basic web vulnerabilities on {target}...")
    try:
        response = requests.get(f"http://{target}", timeout=5)
        headers = response.headers

        issues = []
        if "X-Frame-Options" not in headers:
            issues.append("Missing X-Frame-Options header (Clickjacking risk)")

        if "Content-Security-Policy" not in headers:
            issues.append("Missing Content-Security-Policy header")

        result = "\n".join(issues) if issues else "No basic web header issues found."
        print(result)
        return result
    except Exception as e:
        return f"Web scan failed: {str(e)}"
