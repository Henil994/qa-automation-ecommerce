import re

def sanitize_site_name(site: str) -> str:
    """
    Converts URL or site name into a safe filename.
    Example:
    https://demo.nopcommerce.com
    -> demo_nopcommerce_com
    """
    site = site.lower().strip()
    site = site.replace("https://", "").replace("http://", "")
    site = re.sub(r"[^a-z0-9]+", "_", site)
    return site.strip("_")
