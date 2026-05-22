from configs.llm_config import llm


def analyze_logs(logs):

    print("\n AI Incident Analysis\n")

    for log in logs:

        prompt = f"""
        Analyze this production incident log.

        Service: {log['service']}
        Severity: {log['severity']}
        Message: {log['message']}

        Explain:
        1. What the issue means
        2. Why it may happen
        3. How serious it is
        """

        response = llm.invoke(prompt)

        print(f"\n SERVICE: {log['service']}\n")

        print(response.content)

        print("\n" + "="*60)