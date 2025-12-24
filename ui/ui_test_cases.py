def run_ui_tests(url):
    executed = []
    bugs = []

    scenarios = [
        {
            "scenario_id": "SC_UI_001",
            "module": "UI",
            "feature": "Login",
            "description": "Verify user login with valid credentials",
            "priority": "High"
        }
    ]

    test_cases = [
        {
            "test_case_id": "TC_UI_001",
            "scenario_id": "SC_UI_001",
            "module": "UI",
            "title": "Login with valid credentials",
            "preconditions": "User must be registered",
            "steps": "1. Open login page\n2. Enter valid credentials\n3. Click login",
            "data": "Email: test@test.com | Password: Test@123",
            "expected": "User logged in successfully",
            "actual": "Login button not working",
            "status": "Fail"
        }
    ]

    for tc in test_cases:
        executed.append(tc)
        if tc["status"] == "Fail":
            bugs.append({
                "bug_id": "BUG_UI_001",
                "module": "UI",
                "title": "Login button not responding",
                "description": "Login button does nothing on click",
                "steps": tc["steps"],
                "expected": tc["expected"],
                "actual": tc["actual"],
                "severity": "Critical",
                "priority": "High",
                "status": "Open"
            })

    return scenarios, executed, bugs
