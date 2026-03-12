import streamlit as st
import sqlite3, json

DB_PATH = "../db/verdicts.db"
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

st.title("AI DevOps Log Analyzer Dashboard")

rows = c.execute("SELECT log_hash, result FROM cache").fetchall()

# for h, r in rows:
#     res = json.loads(r)
#     st.write(f"Log Hash: {h}")
#     st.json(res)

for h, r in rows:
    res = json.loads(r)

    st.subheader("Log Analysis Result")

    st.write("**Failure Type:**", res["failure_type"])
    st.write("**Root Cause:**", res["root_cause"])
    st.write("**Suggested Fix:**", res["suggested_fix"])

    st.divider()