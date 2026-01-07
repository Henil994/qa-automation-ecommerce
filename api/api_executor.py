import requests

def execute_api_test(base_url, test_case):
    if "product list" in test_case["title"].lower():
        r = requests.get(f"{base_url}/api/products")
        if r.status_code == 200:
            return "Pass", "200 OK"
        else:
            return "Fail", f"{r.status_code} error"
