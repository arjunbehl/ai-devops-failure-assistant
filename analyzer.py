import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_logs(log_text):

    prompt = f"""
You are an expert DevOps engineer.

Analyze the following CI/CD logs and identify:

- failure_type
- root_cause
- suggested_fix

If the logs do not contain enough information, return:

failure_type: unknown
root_cause: insufficient log information
suggested_fix: collect more logs

Return ONLY JSON in this format:

{{
 "failure_type": "",
 "root_cause": "",
 "suggested_fix": ""
}}

Logs:
{log_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    output = response.choices[0].message.content
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return {
            "failure_type": "parse_error",
            "root_cause": "LLM returned invalid JSON",
            "suggested_fix": "improve prompt or validation"
        }


if __name__ == "__main__":

    with open("logs/dependency_error.log") as f:
        logs = f.read()

    result = analyze_logs(logs)

    print(json.dumps(result,indent=2))