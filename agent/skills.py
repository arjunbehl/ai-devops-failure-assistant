# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from analyzer import analyze_logs
# def get_logs(log_file):
#     path = f"logs/{log_file}"
#     with open(path) as f:
#         return f.read()

# def analyze_log_file(log_file):
#     log_text = get_logs(log_file)
#     return analyze_logs(log_text)

# def search_docs(query):
#     # placeholder for internal doc search
#     return f"Searching docs for '{query}' ... (mock result)"

# def create_ticket(summary, description):
#     # placeholder for creating Jira/GitHub issue
#     return f"Ticket created: {summary} - {description}"
import os, sqlite3, json
from analyzer import analyze_logs
from utils.log_helpers import filter_error_logs, log_hash
from utils.log_helpers import extract_trace_ids, log_hash

DB_PATH = "db/verdicts.db"
os.makedirs("db", exist_ok=True)

# initialize cache DB
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS cache (
    log_hash TEXT PRIMARY KEY,
    result TEXT
)
""")
conn.commit()

def get_logs(location):
    if os.path.exists(location):
        with open(location) as f:
            return f.read()
    else:
        return location  # raw log string

def fetch_trace_logs(trace_id, log_text):
    lines = []
    for line in log_text.split("\n"):
        if f"trace_id={trace_id}" in line:
            lines.append(line)
    return "\n".join(lines)

def analyze_log_file(location):

    log_text = get_logs(location)

    trace_ids = extract_trace_ids(log_text)

    results = []

    for trace in trace_ids:

        trace_logs = fetch_trace_logs(trace, log_text)

        h = log_hash(trace_logs)

        cached = c.execute(
            "SELECT result FROM cache WHERE log_hash=?", (h,)
        ).fetchone()

        if cached:
            results.append(json.loads(cached[0]))
        else:
            res = analyze_logs(trace_logs)

            c.execute(
                "INSERT OR REPLACE INTO cache(log_hash,result) VALUES (?,?)",
                (h, json.dumps(res)),
            )
            conn.commit()

            results.append(res)

    return results