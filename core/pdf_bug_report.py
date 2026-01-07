from fpdf import FPDF
import os
from core.utils import get_timestamp

def generate_bug_pdf(site, bugs):
    os.makedirs("bug_reports", exist_ok=True)

    ts = get_timestamp()
    path = f"bug_reports/{site}_{ts}_bug_report.pdf"

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    pdf.cell(0, 10, "Bug Report", ln=True)

    for bug in bugs:
        pdf.ln(3)
        pdf.multi_cell(0, 8, f"Bug ID: {bug['bug_id']}")
        pdf.multi_cell(0, 8, f"Module: {bug['module']}")
        pdf.multi_cell(0, 8, f"Title: {bug['title']}")
        pdf.multi_cell(0, 8, f"Description: {bug['description']}")
        pdf.multi_cell(0, 8, f"Steps: {bug['steps']}")
        pdf.multi_cell(0, 8, f"Expected: {bug['expected']}")
        pdf.multi_cell(0, 8, f"Actual: {bug['actual']}")
        pdf.multi_cell(0, 8, f"Severity: {bug['severity']}")
        pdf.multi_cell(0, 8, f"Status: {bug['status']}")
        pdf.ln(5)

    pdf.output(path)
    return path
