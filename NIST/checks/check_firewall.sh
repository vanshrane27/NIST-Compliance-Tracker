#!/bin/bash
# SC-7: Firewall configuration
# Ensure this script is executable: chmod +x check_firewall.sh

if command -v ufw >/dev/null 2>&1; then
  status=$(ufw status | grep -i "Status: active")
  default=$(ufw status | grep -i "Default: deny")
  if [[ -n "$status" && -n "$default" ]]; then
    echo '{"control_id": "SC-7", "result": "pass", "details": "UFW is enabled and default deny is set"}'
  else
    echo '{"control_id": "SC-7", "result": "fail", "details": "UFW is not enabled or default deny not set"}'
  fi
elif command -v iptables >/dev/null 2>&1; then
  policy=$(iptables -L | grep "Chain INPUT" -A 1 | grep "policy DROP")
  if [[ -n "$policy" ]]; then
    echo '{"control_id": "SC-7", "result": "pass", "details": "iptables is active with default DROP policy"}'
  else
    echo '{"control_id": "SC-7", "result": "fail", "details": "iptables default policy is not DROP"}'
  fi
else
  echo '{"control_id": "SC-7", "result": "fail", "details": "No firewall (UFW or iptables) found"}'
fi 