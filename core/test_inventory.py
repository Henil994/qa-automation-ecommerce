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
            "steps": "Open login → enter credentials → submit",
            "data": "Various valid/invalid inputs",
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
            "steps": "Add/update/remove product",
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
            "data": "Payment/address variations",
            "expected": "Order placed or error shown",
        })

    return cases
