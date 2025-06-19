#!/bin/bash
# AU-6: Audit log review
# Ensure this script is executable: chmod +x check_audit_logs.sh

rsyslog_status=$(systemctl is-active rsyslog 2>/dev/null)
logrotate_conf="/etc/logrotate.conf"

if [ "$rsyslog_status" != "active" ]; then
  echo '{"control_id": "AU-6", "result": "fail", "details": "rsyslog is not active"}'
  exit 0
fi

if [ ! -f "$logrotate_conf" ]; then
  echo '{"control_id": "AU-6", "result": "fail", "details": "logrotate.conf not found"}'
  exit 0
fi

echo '{"control_id": "AU-6", "result": "pass", "details": "rsyslog is active and logrotate is present"}' 