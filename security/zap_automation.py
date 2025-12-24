from zapv2 import ZAPv2
import time

def run_zap_scan(target):
    zap = ZAPv2(
        proxies={'http': 'http://127.0.0.1:8090',
                 'https': 'http://127.0.0.1:8090'}
    )

    print("[ZAP] Accessing target")
    zap.urlopen(target)
    time.sleep(2)

    print("[ZAP] Spidering")
    scan_id = zap.spider.scan(target)
    while int(zap.spider.status(scan_id)) < 100:
        time.sleep(2)

    print("[ZAP] Active scanning")
    scan_id = zap.ascan.scan(target)
    while int(zap.ascan.status(scan_id)) < 100:
        time.sleep(5)

    return zap.core.alerts()
