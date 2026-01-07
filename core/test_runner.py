from core.utils import sanitize_site_name
from core.excel_test_case import generate_test_case_excel
from core.excel_test_scenario import generate_test_scenario_excel
from core.excel_execution_summary import generate_execution_summary_excel
from core.excel_bug_report import generate_bug_excel
from core.pdf_bug_report import generate_bug_pdf

def execute_all(site, tester, modules):
    safe_site = sanitize_site_name(site)

    all_scenarios, all_tests, all_bugs = [], [], []

    for sc, tc, bg in modules:
        all_scenarios.extend(sc)
        all_tests.extend(tc)
        all_bugs.extend(bg)

    passed = len([t for t in all_tests if t["status"] == "Pass"])
    failed = len([t for t in all_tests if t["status"] == "Fail"])

    generate_test_scenario_excel(safe_site, all_scenarios)
    generate_test_case_excel(safe_site, all_tests)
    generate_execution_summary_excel(safe_site, {
        "total": len(all_tests),
        "executed": len(all_tests),
        "passed": passed,
        "failed": failed,
        "blocked": 0,
        "not_executed": 0,
        "tester": tester
    })

    if all_bugs:
        generate_bug_excel(safe_site, tester, all_bugs)
        generate_bug_pdf(safe_site, all_bugs)
