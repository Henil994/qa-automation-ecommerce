import pandas as pd
import os

def generate_test_scenario_excel(site, scenarios):
    os.makedirs("executed_tests", exist_ok=True)

    rows = []
    for sc in scenarios:
        rows.append({
            "Scenario ID": sc["scenario_id"],
            "Module": sc["module"],
            "Feature": sc["feature"],
            "Scenario Description": sc["description"],
            "Priority": sc["priority"]
        })

    df = pd.DataFrame(rows)
    path = f"executed_tests/{site}_test_scenarios.xlsx"
    df.to_excel(path, index=False)
    return path
