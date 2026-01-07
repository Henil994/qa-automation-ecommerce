from datetime import datetime

def scenario_format(d):
    return f"""
Scenario ID        : {d['scenario_id']}
Module             : {d['module']}
Feature            : {d['feature']}
Scenario Description:
{d['description']}
Priority           : {d['priority']}
"""

def test_case_format(d):
    return f"""
Test Case ID       : {d['test_case_id']}
Scenario ID        : {d['scenario_id']}
Module             : {d['module']}
Test Case Title    : {d['title']}
Preconditions      :
{d['preconditions']}
Test Steps         :
{d['steps']}
Test Data          :
{d['data']}
Expected Result    :
{d['expected']}
Actual Result      :
{d['actual']}
Status             : {d['status']}
"""

def bug_format(d):
    return f"""
Bug ID             : {d['bug_id']}
Module             : {d['module']}
Bug Title          : {d['title']}
Description        :
{d['description']}
Steps to Reproduce :
{d['steps']}
Expected Result    :
{d['expected']}
Actual Result      :
{d['actual']}
Severity           : {d['severity']}
Priority           : {d['priority']}
Status             : {d['status']}
"""

def execution_format(d):
    return f"""
Total Test Cases   : {d['total']}
Executed           : {d['executed']}
Passed             : {d['passed']}
Failed             : {d['failed']}
Blocked            : {d['blocked']}
Not Executed       : {d['not_executed']}
Execution Date     : {datetime.now().strftime('%Y-%m-%d')}
Tester Name        : {d['tester']}
"""
