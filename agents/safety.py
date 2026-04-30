def safety_agent(query):
    if "suicide" in query.lower():
        return "⚠️ Emergency detected. Contact help immediately."
    return None
