from datetime import datetime
import os
from fpdf import FPDF
import re

def generate_report(target, nmap_data, osint_data, web_data):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Sanitize target string to remove http:// and unsafe characters
    safe_target = re.sub(r'[^a-zA-Z0-9_-]', '_', target.replace("http://", "").replace("https://", ""))
    text_filename = f"reports/report_{safe_target}_{timestamp}.txt"
    pdf_filename = f"reports/report_{safe_target}_{timestamp}.pdf"
    os.makedirs("reports", exist_ok=True)

    # Save as plain text
    with open(text_filename, "w") as f:
        f.write(f"SecureSuite Report for {target}\n")
        f.write("=" * 50 + "\n\n")
        f.write("[NMAP SCAN RESULTS]\n")
        f.write(nmap_data + "\n\n")
        f.write("[OSINT INFO]\n")
        f.write(osint_data + "\n\n")
        f.write("[WEB VULNERABILITY SCAN]\n")
        f.write(web_data + "\n\n")

    print(f"[+] Text report saved to {text_filename}")

    # Save as PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    def write_section(title, content):
        pdf.set_text_color(0, 0, 128)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, title, ln=True)

        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", size=11)
        for line in content.splitlines():
            pdf.multi_cell(0, 10, line)

        pdf.ln()

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"SecureSuite Report for {target}", ln=True)
    pdf.ln()

    write_section("NMAP SCAN RESULTS", nmap_data)
    write_section("OSINT INFO", osint_data)
    write_section("WEB VULNERABILITY SCAN", web_data)

    pdf.output(pdf_filename)
    print(f"[+] PDF report saved to {pdf_filename}")
