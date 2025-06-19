#!/bin/bash
# CM-6: System updates and patching
# Ensure this script is executable: chmod +x check_updates.sh

if ! command -v apt >/dev/null 2>&1; then
  echo '{"control_id": "CM-6", "result": "fail", "details": "APT not found (not a Debian/Ubuntu system)"}'
  exit 0
fi

updates=$(apt list --upgradable 2>/dev/null | grep -v "Listing..." | wc -l)
if [ "$updates" -eq 0 ]; then
  echo '{"control_id": "CM-6", "result": "pass", "details": "System is up-to-date"}'
else
  echo '{"control_id": "CM-6", "result": "fail", "details": "'$updates' packages can be updated"}'
fi 