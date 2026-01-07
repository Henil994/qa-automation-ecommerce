import requests
from zapv2 import ZAPv2

ZAP_PROXY = "http://127.0.0.1:8090"

def is_zap_running():
    try:
        requests.get(ZAP_PROXY, timeout=2)
        return True
    except Exception:
        return False

def run_zap_scan(site):
    if not is_zap_running():
        print("[INFO] ZAP not running, skipping dynamic scan.")
        return []

    zap = ZAPv2(proxies={"http": ZAP_PROXY, "https": ZAP_PROXY})
    zap.urlopen(site)
    zap.spider.scan(site)

    while int(zap.spider.status()) < 100:
        pass

    zap.ascan.scan(site)
    while int(zap.ascan.status()) < 100:
        pass

    return zap.core.alerts()
