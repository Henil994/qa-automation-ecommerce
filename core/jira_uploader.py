from jira import JIRA

jira = JIRA(
    server="https://your-domain.atlassian.net",
    basic_auth=("email@example.com", "JIRA_API_TOKEN")
)

def upload_bugs(bugs, project_key):
    for bug in bugs:
        jira.create_issue(fields={
            "project": {"key": project_key},
            "summary": bug["title"],
            "description": f"""
Module: {bug['module']}
Steps: {bug['steps']}
Expected: {bug['expected']}
Actual: {bug['actual']}
""",
            "issuetype": {"name": "Bug"},
            "priority": {"name": bug["priority"]}
        })
