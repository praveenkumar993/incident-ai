from tools.log_tool import fetch_logs

from agents.log_analysis_agent import analyze_logs

from agents.root_cause_agent import (
    identify_root_cause
)

from agents.remediation_agent import (
    suggest_fixes
)

from agents.report_agent import (
    generate_report
)

print("\n Incident AI System Started\n")

logs = fetch_logs()

# Step 1
analyze_logs(logs)

# Step 2
root_causes = identify_root_cause(logs)

# Step 3
fixes = suggest_fixes(root_causes)

# Step 4
generate_report(
    logs,
    root_causes,
    fixes
)