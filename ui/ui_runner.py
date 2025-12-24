from core.test_inventory import ui_test_inventory
from ui.playwright_executor import execute_ui_test

def run_ui_tests(site):
    scenarios = []
    executed = []
    bugs = []

    for tc in ui_test_inventory():
        status, actual = execute_ui_test(site, tc)
        tc["actual"] = actual
        tc["status"] = status
        executed.append(tc)

        if status == "Fail":
            bugs.append({
                "bug_id": f"BUG_{tc['test_case_id']}",
                "module": "UI",
                "title": tc["title"],
                "description": "UI failure detected",
                "steps": tc["steps"],
                "expected": tc["expected"],
                "actual": actual,
                "severity": "High",
                "priority": "High",
                "status": "Open"
            })

    return scenarios, executed, bugs
