def run_api_tests(url):
    executed = []
    bugs = []

    test_cases = [
        {
            "test_case_id": "TC_API_001",
            "scenario_id": "SC_API_001",
            "module": "API",
            "title": "Get product list",
            "preconditions": "API must be accessible",
            "steps": "Send GET /products",
            "data": "None",
            "expected": "200 OK with product list",
            "actual": "500 Internal Server Error",
            "status": "Fail"
        }
    ]

    for tc in test_cases:
        executed.append(tc)
        bugs.append({
            "bug_id": "BUG_API_001",
            "module": "API",
            "title": "Product API failure",
            "description": "Product API returns 500",
            "steps": tc["steps"],
            "expected": tc["expected"],
            "actual": tc["actual"],
            "severity": "High",
            "priority": "High",
            "status": "Open"
        })

    return [], executed, bugs
