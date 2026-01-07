import pandas as pd
import os
from core.utils import get_timestamp

def generate_bug_excel(site, tester, bugs):
    os.makedirs("bug_reports", exist_ok=True)

    rows = []
    for bug in bugs:
        rows.append({
            "Bug ID": bug["bug_id"],
            "Module": bug["module"],
            "Bug Title": bug["title"],
            "Description": bug["description"],
            "Steps to Reproduce": bug["steps"],
            "Expected Result": bug["expected"],
            "Actual Result": bug["actual"],
            "Severity": bug["severity"],
            "Priority": bug["priority"],
            "Status": bug["status"],
            "Reported By": tester
        })

    df = pd.DataFrame(rows)

    ts = get_timestamp()
    path = f"bug_reports/{site}_{ts}_bug_report.xlsx"

    df.to_excel(path, index=False)
    return path
