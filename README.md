# AI DevOps Copilot

AI-powered log analysis system that detects root causes of failures in distributed systems using LLMs.

## Features

- Trace-based log correlation
- Root cause analysis for microservices
- Error-first log processing
- LLM powered explanation
- Caching to reduce API cost
- Streamlit dashboard for visualization

## Architecture

Logs → Error Filter → Trace Correlation → LLM Analysis → Cache DB → Dashboard

## Example Problem

A gateway may return **HTTP 500**, but the real cause could be:

- Authentication failure
- Database timeout
- Downstream service crash

This system detects the **true root cause using trace logs**.

## Setup

Install dependencies

pip install -r requirements.txt

Create `.env`

OPENAI_API_KEY=your_key

Run analyzer

python -m agent.agent

Run dashboard

streamlit run dashboard/dashboard.py

## Sample Output

Failure Type: authentication_failure
Root Cause: login failed due to invalid credentials
Suggested Fix: verify authentication configuration

## Future Improvements

- Splunk / Loki integration
- Kubernetes log streaming
- Semantic evaluation framework
- Automatic alerting
