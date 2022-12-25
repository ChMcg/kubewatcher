import os


log_filename = os.getenv("AUDIT_LOG_PATH") or '/var/lib/rancher/k3s/server/logs/audit.log'

export_api_path = os.getenv("EXPORT_PATH") or "http://analyzer:8000/receiver/audit"
