def risk_agent(query):
    q = query.lower()
    if "chest pain" in q:
        return "🔴 HIGH RISK"
    elif "fever" in q:
        return "🟠 MEDIUM RISK"
    return "🟢 LOW RISK"
