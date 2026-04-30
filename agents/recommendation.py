def recommendation_agent(risk):
    if "HIGH" in risk:
        return "Seek immediate medical attention."
    elif "MEDIUM" in risk:
        return "Rest and monitor symptoms."
    return "Stay hydrated and rest."
