import os
import subprocess
import json
from datetime import datetime

# Optional: for colored output
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORAMA = True
except ImportError:
    COLORAMA = False

# Paths
CHECKS_DIR = os.path.join(os.path.dirname(__file__), 'checks')
REPORTS_DIR = os.path.join(os.path.dirname(__file__), 'reports')
MAP_FILE = os.path.join(os.path.dirname(__file__), 'controls_map.json')
OUTPUT_FILE = os.path.join(REPORTS_DIR, 'output.json')

# Load control mappings
def load_controls_map():
    with open(MAP_FILE, 'r') as f:
        return json.load(f)

# Run a single check script and parse its output
def run_check(script_path):
    try:
        result = subprocess.run(['bash', script_path], capture_output=True, text=True, timeout=30)
        output = result.stdout.strip()
        return json.loads(output)
    except Exception as e:
        return {"result": "fail", "details": f"Error running {os.path.basename(script_path)}: {e}"}

# Main orchestrator
def main():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    controls_map = load_controls_map()
    results = []
    pass_count = 0
    fail_count = 0

    for control in controls_map:
        script = control['script']
        script_path = os.path.join(CHECKS_DIR, script)
        if not os.path.exists(script_path):
            results.append({
                "control_id": control['control_id'],
                "control_name": control['control_name'],
                "result": "fail",
                "details": f"Script {script} not found."
            })
            fail_count += 1
            continue
        check_result = run_check(script_path)
        # Merge control info
        entry = {
            "control_id": control['control_id'],
            "control_name": control['control_name'],
            "result": check_result.get('result', 'fail'),
            "details": check_result.get('details', '')
        }
        if entry['result'] == 'pass':
            pass_count += 1
        else:
            fail_count += 1
        results.append(entry)

    # Save to JSON
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(results, f, indent=2)

    # Print summary
    print(f"\nNIST Compliance Tracker - Audit Results ({datetime.now().strftime('%Y-%m-%d %H:%M')})\n")
    for entry in results:
        status = entry['result'].upper()
        if COLORAMA:
            color = Fore.GREEN if status == 'PASS' else Fore.RED
            print(f"{color}{status}{Style.RESET_ALL} - {entry['control_id']} ({entry['control_name']}): {entry['details']}")
        else:
            print(f"{status} - {entry['control_id']} ({entry['control_name']}): {entry['details']}")
    total = pass_count + fail_count
    print(f"\nSummary: {pass_count}/{total} passed, {fail_count}/{total} failed.")

if __name__ == '__main__':
    main() 