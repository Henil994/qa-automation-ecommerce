from api.api_executor import execute_api_test

def run_api_tests(site):
    test_cases = [
        {
            "test_case_id": "TC_API_001",
            "scenario_id": "SC_API_PRODUCT",
            "module": "API",
            "title": "Get product list",
            "preconditions": "API live",
            "steps": "GET /api/products",
            "data": "None",
            "expected": "200 OK"
        }
    ]

    executed, bugs = [], []

    for tc in test_cases:
        status, actual = execute_api_test(site, tc)
        tc["actual"] = actual
        tc["status"] = status
        executed.append(tc)

        if status == "Fail":
            bugs.append({
                "bug_id": "BUG_API_001",
                "module": "API",
                "title": tc["title"],
                "description": "API failure",
                "steps": tc["steps"],
                "expected": tc["expected"],
                "actual": actual,
                "severity": "High",
                "priority": "High",
                "status": "Open"
            })

    return [], executed, bugs
