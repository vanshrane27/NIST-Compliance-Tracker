#!/bin/bash
# AC-17: Remote access (SSH)
# Ensure this script is executable: chmod +x check_ssh.sh

sshd_config="/etc/ssh/sshd_config"
if [ ! -f "$sshd_config" ]; then
  echo '{"control_id": "AC-17", "result": "fail", "details": "sshd_config not found"}'
  exit 0
fi

permit_root=$(grep -Ei '^PermitRootLogin' $sshd_config | grep -i 'no')
password_auth=$(grep -Ei '^PasswordAuthentication' $sshd_config | grep -i 'no')

if [[ -n "$permit_root" && -n "$password_auth" ]]; then
  echo '{"control_id": "AC-17", "result": "pass", "details": "Root login and password authentication are disabled"}'
else
  details=""
  if [ -z "$permit_root" ]; then details="PermitRootLogin is not set to no. "; fi
  if [ -z "$password_auth" ]; then details+="PasswordAuthentication is not set to no."; fi
  echo '{"control_id": "AC-17", "result": "fail", "details": "'$details'"}'
fi 