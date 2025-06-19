# NIST Compliance Tracker

NIST Compliance Tracker is a lightweight, script-based security auditing tool for Linux systems. It automates the assessment of key system settings against NIST SP 800-53 controls, providing actionable compliance insights for system administrators, auditors, and security professionals.

---

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [Folder Structure](#folder-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Controls Covered](#controls-covered)
- [PDF Report Generation](#pdf-report-generation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Features
- **Automated NIST SP 800-53 checks**: Maps each check to a specific NIST control (e.g., AC-2, AU-6, SC-7, etc.)
- **Script-based, modular design**: Each check is a standalone Bash script for easy customization and extension
- **Multi-format output**: Results are displayed in the terminal, saved as JSON, and can be exported to PDF
- **Safe, read-only**: All checks are non-intrusive and do not modify system settings
- **Remediation guidance**: Output includes suggestions for failed checks

---

## How It Works
- The main orchestrator (`audit.py`) loads a mapping of NIST controls to check scripts from `controls_map.json`.
- Each check script in `checks/` runs a specific system audit and outputs a JSON result.
- Results are aggregated, summarized, and saved to `reports/output.json`.
- Optionally, results can be exported to a PDF report using inbuilt Linux tools (`pandoc` or `wkhtmltopdf`).

---

## Folder Structure
```
NIST/
├── audit.py                # Main orchestrator script
├── checks/                 # Bash scripts for each NIST control
│   ├── check_firewall.sh
│   ├── check_users.sh
│   ├── check_updates.sh
│   ├── check_ssh.sh
│   ├── check_password_policy.sh
│   └── check_audit_logs.sh
├── controls_map.json       # Mapping of controls to scripts
├── reports/                # Output directory for results
│   └── output.json
├── utils/
│   └── report_to_pdf.py    # PDF export utility (uses pandoc/wkhtmltopdf)
├── README.md
├── requirements.txt        # Python dependencies (for optional features)
```

---

## Setup
1. **System Requirements:**
   - Python 3.x
   - Bash shell
   - Linux (Debian/Ubuntu/Kali recommended)
   - For PDF export: `pandoc` or `wkhtmltopdf` (install via `sudo apt install pandoc` or `sudo apt install wkhtmltopdf`)
2. **Clone the repository:**
   ```bash
   git clone https://github.com/vanshrane27/NIST-Compliance-Tracker.git
   cd NIST-Compliance-Tracker/NIST
   ```
3. **(Recommended) Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Make check scripts executable:**
   ```bash
   chmod +x checks/*.sh
   ```

---

## Usage
1. **Run the audit:**
   ```bash
   python audit.py
   ```
   - Results are displayed in the terminal and saved to `reports/output.json`.

2. **Export results to PDF:**
   ```bash
   python utils/report_to_pdf.py
   ```
   - This will generate `reports/audit_report.pdf` using `pandoc` or `wkhtmltopdf`.
   - If neither tool is installed, the script will prompt you to install one.

---

## Sample Output
```
[
  {
    "control_id": "AC-2",
    "control_name": "Account Management",
    "result": "fail",
    "details": "2 inactive accounts found: guest, testuser"
  },
  {
    "control_id": "SC-7",
    "control_name": "Boundary Protection",
    "result": "pass",
    "details": "UFW is enabled and configured with default deny"
  }
]
```

---

## Controls Covered
| Control | Description |
|---------|-------------|
| AC-2    | User account management |
| AU-6    | Audit log review |
| SC-7    | Firewall configuration |
| CM-6    | System updates and patching |
| IA-2    | Authentication (password policy) |
| AC-17   | Remote access (SSH) |

---

## PDF Report Generation
- The PDF export utility (`utils/report_to_pdf.py`) converts the JSON results to a styled HTML report, then uses `pandoc` or `wkhtmltopdf` to generate a PDF.
- **Dependencies:**
  - Install `pandoc` or `wkhtmltopdf` if you want PDF export:
    ```bash
    sudo apt install pandoc
    # or
    sudo apt install wkhtmltopdf
    ```
- The script will automatically detect and use whichever tool is available.

---

## Troubleshooting
- **Permission denied running scripts:**
  - Ensure all check scripts are executable: `chmod +x checks/*.sh`
- **Python package/module not found:**
  - Activate your virtual environment and reinstall requirements: `source venv/bin/activate && pip install -r requirements.txt`
- **PDF not generated:**
  - Make sure `pandoc` or `wkhtmltopdf` is installed and accessible in your PATH.
- **Systemd service errors (e.g., rsyslog):**
  - Install missing services using your package manager (e.g., `sudo apt install rsyslog`).

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch for your feature or fix
3. Commit your changes with clear messages
4. Open a pull request describing your changes

---
![WhatsApp Image 2025-06-19 at 2 33 40 PM](https://github.com/user-attachments/assets/8da15150-a733-45bf-8b3c-0bd843e37042)


![WhatsApp Image 2025-06-19 at 2 33 40 PM (1)](https://github.com/user-attachments/assets/35526e77-fef8-4e03-9633-1b91ec005a31)


![WhatsApp Image 2025-06-19 at 2 33 40 PM (2)](https://github.com/user-attachments/assets/c8b53f81-a8e2-4d95-b4a6-efc0a6247718)
