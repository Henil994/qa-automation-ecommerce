from fpdf import FPDF
import os

def generate_bug_pdf(site, bugs):
    os.makedirs("bug_reports", exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    for bug in bugs:
        pdf.multi_cell(0, 8, f"""
Bug ID: {bug['bug_id']}
Module: {bug['module']}
Title: {bug['title']}
Severity: {bug['severity']}
Priority: {bug['priority']}
Status: {bug['status']}

Description:
{bug['description']}

Steps:
{bug['steps']}

Expected:
{bug['expected']}

Actual:
{bug['actual']}
---------------------------
""")

    path = f"bug_reports/{site}_bug_report.pdf"
    pdf.output(path)
    return path
