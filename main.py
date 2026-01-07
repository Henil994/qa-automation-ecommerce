from ui.ui_tests import run_ui_tests
from api.api_tests import run_api_tests
from database.db_tests import run_db_tests
from performance.performance_tests import run_performance_tests
from security.security_tests import run_security_tests
from accessibility.accessibility_tests import run_accessibility_tests
from core.test_runner import execute_all

site = "demo_ecommerce"
tester = "Henil"

modules = [
    run_ui_tests(site),
    run_api_tests(site),
    run_db_tests(site),
    run_performance_tests(site),
    run_security_tests(site),
    run_accessibility_tests(site)
]

execute_all(site, tester, modules)
