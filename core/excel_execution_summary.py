import pandas as pd
import os
from core.utils import get_timestamp

def generate_execution_summary_excel(site, summary):
    os.makedirs("executed_tests", exist_ok=True)

    ts = get_timestamp()
    path = f"executed_tests/{site}_{ts}_execution_summary.xlsx"

    df = pd.DataFrame([{
        "Total Test Cases": summary["total"],
        "Executed": summary["executed"],
        "Passed": summary["passed"],
        "Failed": summary["failed"],
        "Blocked": summary["blocked"],
        "Not Executed": summary["not_executed"],
        "Execution Date": ts,
        "Tester Name": summary["tester"]
    }])

    df.to_excel(path, index=False)
    return path
