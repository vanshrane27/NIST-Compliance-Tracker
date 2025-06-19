# NIST Compliance Tracker

A lightweight, script-based security auditing tool for Linux systems, mapping checks to NIST SP 800-53 controls.

## Features
- Audits key system settings for compliance readiness
- Maps each check to a NIST control (e.g., AC-2, AU-6, SC-7, etc.)
- Outputs results in terminal, JSON, and optionally PDF
- Safe, read-only checks (no system changes)

## Folder Structure
```
NIST/
├── audit.py
├── checks/
│   ├── check_firewall.sh
│   ├── check_users.sh
│   ├── check_updates.sh
│   ├── check_ssh.sh
│   └── check_password_policy.sh
├── controls_map.json
├── reports/
│   └── output.json
├── utils/
│   └── report_to_pdf.py
├── README.md
├── requirements.txt
```

## Setup
1. Ensure Python 3 and Bash are installed (Ubuntu/Debian recommended).
2. Clone/download this repo.
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run
```bash
python3 audit.py
```
- Results are shown in terminal and saved to `reports/output.json`.
- (Optional) Export to PDF:
  ```bash
  python3 utils/report_to_pdf.py
  ```

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

## Controls Covered
| Control | Description |
|---------|-------------|
| AC-2    | User account management |
| AU-6    | Audit log review |
| SC-7    | Firewall configuration |
| CM-6    | System updates and patching |
| IA-2    | Authentication (password policy) |
| AC-17   | Remote access (SSH) |

## Notes
- All checks are non-intrusive and safe for test environments.
- For educational and compliance-readiness use only.

## Optional Features
- PDF export of results
- Terminal coloring for pass/fail
- Remediation suggestions for failed checks 