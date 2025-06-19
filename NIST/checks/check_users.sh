#!/bin/bash
# AC-2: User account management
# Ensure this script is executable: chmod +x check_users.sh

inactive_users=$(awk -F: '($2!="*" && $2!="!" && $7!="/usr/sbin/nologin" && $7!="/bin/false") {print $1}' /etc/shadow | while read user; do
    lastlog -u "$user" | grep -q "Never logged in" && echo "$user"
done)

if [ -z "$inactive_users" ]; then
  echo '{"control_id": "AC-2", "result": "pass", "details": "No inactive users found"}'
else
  echo '{"control_id": "AC-2", "result": "fail", "details": "Inactive accounts found: '$(echo $inactive_users | tr '\n' ', ' | sed 's/, $//')'"}'
fi 