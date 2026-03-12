import hashlib
import re


def filter_error_logs(log_text):
    return [line for line in log_text.split("\n") if "ERROR" in line or "500" in line]


def extract_trace_ids(log_text):
    trace_ids = set()

    for line in log_text.split("\n"):
        if "ERROR" in line or "500" in line:
            match = re.search(r"trace_id=([a-zA-Z0-9\-]+)", line)
            if match:
                trace_ids.add(match.group(1))

    return list(trace_ids)


def log_hash(log_text):
    return hashlib.sha256(log_text.encode()).hexdigest()