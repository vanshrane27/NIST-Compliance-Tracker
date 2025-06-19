import json
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

REPORTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'reports')
OUTPUT_FILE = os.path.join(REPORTS_DIR, 'output.json')
PDF_FILE = os.path.join(REPORTS_DIR, 'audit_report.pdf')

def generate_pdf(data, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    y = height - 40
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y, "NIST Compliance Tracker - Audit Report")
    y -= 30
    c.setFont("Helvetica", 10)
    for entry in data:
        color = colors.green if entry['result'] == 'pass' else colors.red
        c.setFillColor(color)
        c.drawString(40, y, f"{entry['control_id']} - {entry['control_name']} [{entry['result'].upper()}]")
        c.setFillColor(colors.black)
        y -= 15
        c.drawString(60, y, f"Details: {entry['details']}")
        y -= 20
        if y < 60:
            c.showPage()
            y = height - 40
    c.save()

def main():
    if not os.path.exists(OUTPUT_FILE):
        print("No audit output found. Run audit.py first.")
        return
    with open(OUTPUT_FILE, 'r') as f:
        data = json.load(f)
    generate_pdf(data, PDF_FILE)
    print(f"PDF report generated: {PDF_FILE}")

if __name__ == '__main__':
    main() 