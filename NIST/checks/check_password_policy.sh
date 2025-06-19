#!/bin/bash
# IA-2: Authentication (password policy)
# Ensure this script is executable: chmod +x check_password_policy.sh

defs="/etc/login.defs"
if [ ! -f "$defs" ]; then
  echo '{"control_id": "IA-2", "result": "fail", "details": "login.defs not found"}'
  exit 0
fi

minlen=$(grep -E '^PASS_MIN_LEN' $defs | awk '{print $2}')
maxdays=$(grep -E '^PASS_MAX_DAYS' $defs | awk '{print $2}')
mindays=$(grep -E '^PASS_MIN_DAYS' $defs | awk '{print $2}')

if [ "$minlen" -ge 12 ] && [ "$maxdays" -le 90 ] && [ "$mindays" -ge 1 ]; then
  echo '{"control_id": "IA-2", "result": "pass", "details": "Password policy meets minimum requirements"}'
else
  details=""
  if [ "$minlen" -lt 12 ]; then details="PASS_MIN_LEN is less than 12. "; fi
  if [ "$maxdays" -gt 90 ]; then details+="PASS_MAX_DAYS is more than 90. "; fi
  if [ "$mindays" -lt 1 ]; then details+="PASS_MIN_DAYS is less than 1."; fi
  echo '{"control_id": "IA-2", "result": "fail", "details": "'$details'"}'
fi 