import pandas as pd
import os

def generate_test_case_excel(site, test_cases):
    os.makedirs("executed_tests", exist_ok=True)

    rows = []
    for tc in test_cases:
        rows.append({
            "Test Case ID": tc["test_case_id"],
            "Scenario ID": tc["scenario_id"],
            "Module": tc["module"],
            "Test Case Title": tc["title"],
            "Preconditions": tc["preconditions"],
            "Test Steps": tc["steps"],
            "Test Data": tc["data"],
            "Expected Result": tc["expected"],
            "Actual Result": tc["actual"],
            "Status": tc["status"]
        })

    df = pd.DataFrame(rows)
    path = f"executed_tests/{site}_test_cases.xlsx"
    df.to_excel(path, index=False)
    return path
