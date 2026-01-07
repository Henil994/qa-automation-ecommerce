# ================= UI INVENTORY =================

def ui_test_inventory():
    cases = []

    # AUTHENTICATION (15)
    for i in range(1, 16):
        cases.append({
            "test_case_id": f"TC_UI_AUTH_{i:03}",
            "scenario_id": "SC_UI_AUTH",
            "module": "UI",
            "title": f"Login validation case {i}",
            "preconditions": "User exists",
            "steps": "Open login -> enter credentials -> submit",
            "data": "Valid and invalid credentials",
            "expected": "Correct login behavior",
        })

    # CART (20)
    for i in range(1, 21):
        cases.append({
            "test_case_id": f"TC_UI_CART_{i:03}",
            "scenario_id": "SC_UI_CART",
            "module": "UI",
            "title": f"Cart operation case {i}",
            "preconditions": "Product exists",
            "steps": "Add, update, remove product",
            "data": "Different quantities",
            "expected": "Cart updates correctly",
        })

    # CHECKOUT (25)
    for i in range(1, 26):
        cases.append({
            "test_case_id": f"TC_UI_CHECKOUT_{i:03}",
            "scenario_id": "SC_UI_CHECKOUT",
            "module": "UI",
            "title": f"Checkout flow case {i}",
            "preconditions": "Cart not empty",
            "steps": "Proceed to checkout",
            "data": "Payment and address variations",
            "expected": "Order placed or error shown",
        })

    return cases


# ================= API INVENTORY =================

def api_test_inventory():
    cases = []
    for i in range(1, 31):
        cases.append({
            "test_case_id": f"TC_API_{i:03}",
            "scenario_id": "SC_API_ALL",
            "module": "API",
            "title": f"API validation case {i}",
            "preconditions": "API available",
            "steps": "Send API request",
            "data": "JSON payload",
            "expected": "Correct API response",
        })
    return cases


# ================= DATABASE INVENTORY =================

def db_test_inventory():
    cases = []
    for i in range(1, 16):
        cases.append({
            "test_case_id": f"TC_DB_{i:03}",
            "scenario_id": "SC_DB_ALL",
            "module": "Database",
            "title": f"Database validation case {i}",
            "preconditions": "Database connected",
            "steps": "Execute SQL query",
            "data": "Table and record",
            "expected": "Data integrity maintained",
        })
    return cases


# ================= PERFORMANCE INVENTORY =================

def performance_test_inventory():
    cases = []
    for i in range(1, 16):
        cases.append({
            "test_case_id": f"TC_PERF_{i:03}",
            "scenario_id": "SC_PERF_ALL",
            "module": "Performance",
            "title": f"Performance SLA case {i}",
            "preconditions": "System under load",
            "steps": "Run load test",
            "data": "Concurrent users",
            "expected": "SLA met",
        })
    return cases


# ================= ACCESSIBILITY INVENTORY =================

def accessibility_test_inventory():
    cases = []
    for i in range(1, 11):
        cases.append({
            "test_case_id": f"TC_ACC_{i:03}",
            "scenario_id": "SC_ACC_ALL",
            "module": "Accessibility",
            "title": f"Accessibility rule case {i}",
            "preconditions": "Page loaded",
            "steps": "Validate WCAG rule",
            "data": "UI element",
            "expected": "WCAG compliant",
        })
    return cases


# ================= SECURITY INVENTORY =================

def security_test_inventory():
    cases = []
    for i in range(1, 21):
        cases.append({
            "test_case_id": f"TC_SEC_{i:03}",
            "scenario_id": "SC_SEC_ALL",
            "module": "Security",
            "title": f"Security test case {i}",
            "preconditions": "Application running",
            "steps": "Attempt attack vector",
            "data": "Malicious payload",
            "expected": "Attack blocked",
        })
    return cases
