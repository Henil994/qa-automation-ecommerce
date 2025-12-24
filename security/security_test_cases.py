from security.zap_automation import run_zap_scan

def run_security_tests(site):
    alerts = run_zap_scan(site)

    test_cases = []
    bugs = []

    for alert in alerts:
        test_cases.append({
            "test_case_id": f"TC_ZAP_{alert['pluginId']}",
            "scenario_id": "SC_SEC_ZAP",
            "module": "Security",
            "title": alert["alert"],
            "preconditions": "ZAP scan",
            "steps": alert["url"],
            "data": alert["param"],
            "expected": "No vulnerability",
            "actual": alert["desc"],
            "status": "Fail"
        })

        bugs.append({
            "bug_id": f"BUG_ZAP_{alert['pluginId']}",
            "module": "Security",
            "title": alert["alert"],
            "description": alert["desc"],
            "steps": alert["url"],
            "expected": "Secure application",
            "actual": alert["desc"],
            "severity": alert["risk"],
            "priority": "High",
            "status": "Open"
        })

    return [], test_cases, bugs
