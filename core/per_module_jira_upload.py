from core.jira_uploader import upload_bugs

if all_bugs:
    upload_bugs([b for b in all_bugs if b["module"] == "UI"], "UIBUG")
    upload_bugs([b for b in all_bugs if b["module"] == "API"], "APIBUG")
