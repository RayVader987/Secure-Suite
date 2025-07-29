# SecureSuite: VAPT + OSINT Tool

Welcome to **SecureSuite** — a simple yet powerful open-source tool designed to perform Vulnerability Assessment and Penetration Testing (VAPT) combined with OSINT (Open Source Intelligence) gathering. This project is built to help security enthusiasts and beginners explore basic network scanning, web vulnerability checks, and information gathering, all wrapped up in a clean, automated workflow.

---

## What Does SecureSuite Do?

SecureSuite takes an IP address or domain as input and runs several automated security checks, including:

- **Nmap scanning:** to detect open ports and running services.
- **OSINT lookups:** such as WHOIS information and DNS queries to gather public data about the target.
- **Basic Web Vulnerability Scanning:** checks for common HTTP security headers to flag potential risks.
- **Report Generation:** creates detailed reports in both plain text and PDF formats for easy sharing and analysis.

## How to Get Started

### 1. Clone or Download the Project

```bash
git clone https://github.com/RayVader987/SecureSuite.git
```
### 2. Set up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the tool
```bash
python3 main.py
```
You will be prompted to enter a target IP or domain(without the http:// prefix, e.g., testphp.vulnweb.com)

## Project Structure
SecureSuite/
├── main.py                  # Entry point of the tool
├── modules/                 # Core modules for scanning, OSINT, and reporting
│   ├── __init__.py
│   ├── nmap_scan.py
│   ├── osint_lookup.py
│   ├── web_scanner.py
│   └── report_generator.py
├── reports/                 # Generated text and PDF reports will be saved here
├── requirements.txt         # Python dependencies
└── README.md                # This file

## Sample Usage
1. Run the program and enter a target IP or domain

2. The tool will perform an Nmap scan, gather WHOIS and DNS info, check web vulnerabilities, and then generate a report.

3. Reports are saved inside the reports/ folder as both .txt and .pdf files.

4. Open and review the reports to analyze findings.

## Disclaimer
This tool is meant for educational and authorized security testing purposes only. Always ensure you have explicit permission before scanning any network or website.



