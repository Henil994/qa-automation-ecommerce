import re
from datetime import datetime


def sanitize_site_name(site: str) -> str:
    """
    Convert a website URL into a safe filename.
    Example:
    https://demo.nopcommerce.com -> demo_nopcommerce_com
    """
    if not site:
        return "unknown_site"

    site = site.strip().lower()
    site = site.replace("https://", "").replace("http://", "")
    site = re.sub(r"[^a-z0-9]+", "_", site)
    return site.strip("_")


def get_timestamp() -> str:
    """
    Return current timestamp for reports.
    Format: YYYYMMDD_HHMMSS
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")
