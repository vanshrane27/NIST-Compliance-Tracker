import json
import os
import subprocess
import sys
import tempfile

REPORTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'reports')
OUTPUT_FILE = os.path.join(REPORTS_DIR, 'output.json')
PDF_FILE = os.path.join(REPORTS_DIR, 'audit_report.pdf')

HTML_TEMPLATE = """
<html>
<head><meta charset='utf-8'><title>NIST Compliance Tracker - Audit Report</title></head>
<body>
<h1>NIST Compliance Tracker - Audit Report</h1>
{body}
</body>
</html>
"""

def generate_html(data):
    body = ""
    for entry in data:
        color = "green" if entry['result'] == 'pass' else 'red'
        body += f"<h3 style='color:{color};'>{entry['control_id']} - {entry['control_name']} [{entry['result'].upper()}]</h3>"
        body += f"<p>Details: {entry['details']}</p>"
    return HTML_TEMPLATE.format(body=body)

def convert_html_to_pdf(html_path, pdf_path):
    # Try wkhtmltopdf first, then pandoc
    try:
        subprocess.run(['wkhtmltopdf', html_path, pdf_path], check=True)
        return True
    except FileNotFoundError:
        pass
    except subprocess.CalledProcessError:
        print("Error: wkhtmltopdf failed.")
        return False
    try:
        subprocess.run(['pandoc', html_path, '-o', pdf_path], check=True)
        return True
    except FileNotFoundError:
        print("Error: Neither wkhtmltopdf nor pandoc is installed.")
        return False
    except subprocess.CalledProcessError:
        print("Error: pandoc failed.")
        return False

def main():
    if not os.path.exists(OUTPUT_FILE):
        print("No audit output found. Run audit.py first.")
        return
    with open(OUTPUT_FILE, 'r') as f:
        data = json.load(f)
    html_content = generate_html(data)
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as tmp_html:
        tmp_html.write(html_content)
        html_path = tmp_html.name
    success = convert_html_to_pdf(html_path, PDF_FILE)
    os.remove(html_path)
    if success:
        print(f"PDF report generated: {PDF_FILE}")
    else:
        print("Failed to generate PDF report. Please ensure wkhtmltopdf or pandoc is installed.")

if __name__ == '__main__':
    main() 