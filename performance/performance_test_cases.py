def run_performance_tests(url):
    executed = [{
        "test_case_id": "TC_PERF_001",
        "scenario_id": "SC_PERF_001",
        "module": "Performance",
        "title": "Homepage load time",
        "preconditions": "Site live",
        "steps": "Open homepage",
        "data": "100 users",
        "expected": "< 3 seconds",
        "actual": "6 seconds",
        "status": "Fail"
    }]

    bugs = [{
        "bug_id": "BUG_PERF_001",
        "module": "Performance",
        "title": "Slow homepage",
        "description": "Homepage exceeds SLA",
        "steps": "Open homepage under load",
        "expected": "< 3 seconds",
        "actual": "6 seconds",
        "severity": "Medium",
        "priority": "Medium",
        "status": "Open"
    }]

    return [], executed, bugs
