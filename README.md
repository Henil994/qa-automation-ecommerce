# 🧪 Enterprise QA Automation Framework (E-Commerce)

An **end-to-end QA automation framework** for e-commerce websites, built on **Python** with a **GUI-driven execution model**.  
It supports **UI, API, Database, Performance, Security, and Accessibility testing**, with **centralized reporting** in Excel and PDF formats.

This project is designed to demonstrate **enterprise-level QA automation architecture**, not just isolated test scripts.

## 🚀 Key Features

- ✅ GUI-based test execution (Tkinter)
- ✅ Modular test execution (UI / API / DB / Performance / Security / Accessibility)
- ✅ Inventory-driven test case management
- ✅ 150+ enterprise-style test cases
- ✅ Excel reports:
  - Test Scenarios
  - Test Cases
  - Execution Summary
  - Bug Reports
- ✅ PDF bug report generation
- ✅ Optional OWASP ZAP integration
- ✅ Optional Locust load testing
- ✅ Clean, extensible architecture
- 
## 🧱 Project Structure

qa_automation_ecommerce/
│
├── gui.py # GUI to run tests
├── requirements.txt # Python dependencies
├── README.md
│
├── core/
│ ├── test_inventory.py # All test case definitions (150+)
│ ├── test_runner.py # Central execution engine
│ ├── utils.py # Common helpers
│ ├── excel_test_case.py
│ ├── excel_test_scenario.py
│ ├── excel_execution_summary.py
│ ├── excel_bug_report.py
│ └── pdf_bug_report.py
│
├── ui/
│ └── ui_test_cases.py
│
├── api/
│ └── api_test_cases.py
│
├── database/
│ └── db_test_cases.py
│
├── performance/
│ ├── performance_test_cases.py
│ └── locustfile.py
│
├── security/
│ ├── security_test_cases.py
│ └── zap_automation.py
│
├── accessibility/
│ └── accessibility_test_cases.py
│
├── executed_tests/ # Generated Excel execution reports
└── bug_reports/ # Generated bug reports (Excel + PDF)

## 🧪 Test Coverage

| Module | Test Cases |
|------|-----------|
| UI Testing | 60 |
| API Testing | 30 |
| Database Testing | 15 |
| Performance Testing | 15 |
| Security Testing | 20 |
| Accessibility Testing | 10 |
| **Total** | **150** |

## 🖥️ GUI Capabilities

- Enter target website URL
- Enter tester name
- Select test modules using checkboxes
- Run tests asynchronously (GUI never freezes)
- Generate reports automatically

## 📊 Reports Generated

All reports are generated automatically after execution:

### 📁 `executed_tests/`
- `<site>_test_cases.xlsx`
- `<site>_test_scenarios.xlsx`
- `<site>_execution_summary.xlsx`

### 📁 `bug_reports/`
- `<site>_bug_report.xlsx`
- `<site>_bug_report.pdf`

File names are automatically sanitized based on the website URL.

## ⚙️ Installation & Setup (Kali Linux)

### 1️⃣ Clone the repository

git clone git@github.com:Henil994/qa-automation-ecommerce.git
cd qa_automation_ecommerce

2️⃣ Create virtual environment

python3 -m venv myenv
source myenv/bin/activate

3️⃣ Install dependencies

pip install -r requirements.txt

▶️ How to Run

python3 gui.py
Example input:
Website URL: https://demo.nopcommerce.com
Tester Name: Henil

Select required modules → Click Run Tests

🔐 Security Testing (Optional)
This framework supports OWASP ZAP.

If ZAP is running → dynamic security scan runs
If ZAP is not running → security tests still execute (gracefully skipped)

Start ZAP in daemon mode (Kali Linux):

zaproxy -daemon -port 8090 -config api.disablekey=true
🚀 Performance Testing (Optional)
Uses Locust in headless mode.

Install Locust:

pip install locust
Performance tests run asynchronously and do not block reporting.

🧠 Design Philosophy

Inventory-driven test management
Clear separation of concerns
Execution ≠ Inventory
Reporting centralized in core layer
External tools are optional and non-blocking

📌 Interview Talking Points

Modular automation architecture
Inventory vs execution validation
GUI-driven execution
Enterprise-style reporting
Optional tool integration (ZAP, Locust)
Clean Git workflow and project structure

📈 Future Enhancements

Playwright-based real UI automation
Real API assertions
SLA-based performance thresholds
CI/CD with GitHub Actions
Jira integration
HTML dashboard reporting

👤 Author

Henil
QA Automation Engineer
Focused on enterprise-grade test frameworks and tooling.

📄 License
This project is for learning, demonstration, and portfolio use.


