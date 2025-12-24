import pandas as pd
import os
from datetime import datetime

def generate_execution_summary_excel(site, summary):
    os.makedirs("executed_tests", exist_ok=True)

    df = pd.DataFrame([{
        "Total Test Cases": summary["total"],
        "Executed": summary["executed"],
        "Passed": summary["passed"],
        "Failed": summary["failed"],
        "Blocked": summary["blocked"],
        "Not Executed": summary["not_executed"],
        "Execution Date": datetime.now().strftime("%Y-%m-%d"),
        "Tester Name": summary["tester"]
    }])

    path = f"executed_tests/{site}_execution_summary.xlsx"
    df.to_excel(path, index=False)
    return path
