from modules import nmap_scan, osint_lookup, web_scanner, report_generator
import re 

def main():
    print("==== SecureSuite: VAPT + OSINT Tool ====")
    target = input("Enter target IP or domain: ").strip()
    # Extract only domain or IP (removes http://, https://, trailing slashes)
    clean_target = re.sub(r'^https?://', '', target).split('/')[0]


    print("\n[1] Running Nmap Scan...")
    nmap_result = nmap_scan.run_nmap(target)

    print("\n[2] Gathering OSINT Information...")
    osint_result = osint_lookup.run_osint(target)

    print("\n[3] Performing Web Vulnerability Scan...")
    web_vuln_result = web_scanner.scan_web(target)

    print("\n[4] Generating Report...")
    report_generator.generate_report(target, nmap_result, osint_result, web_vuln_result)

    print("\n✅ Scan Complete. Report saved in /reports")

if __name__ == "__main__":
    main()
