import pandas as pd
import os
from datetime import datetime

def generate_bug_excel(site, tester, bug_list):
    os.makedirs("bug_reports", exist_ok=True)

    rows = []
    for bug in bug_list:
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
            "Website": site,
            "Reported Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Tester Name": tester
        })

    df = pd.DataFrame(rows)
    file_path = f"bug_reports/{site}_bug_report.xlsx"
    df.to_excel(file_path, index=False)

    return file_path
