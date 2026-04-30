import gradio as gr
from agents.safety import safety_agent
from agents.risk import risk_agent
from agents.recommendation import recommendation_agent
from rag.retriever import retrieve_context
from llm.model import generate_response

def system(query, history):
    safety = safety_agent(query)
    if safety:
        return safety

    risk = risk_agent(query)
    recommendation = recommendation_agent(risk)
    context = retrieve_context(query)

    response = generate_response(query, risk, recommendation, context)

    return f"""
{risk}

💊 Recommendation:
{recommendation}

🤖 AI Advice:
{response}

⚠️ Disclaimer: This is not a medical diagnosis.
""".strip()

def chat_fn(message, history):
    response = system(message, history)
    history.append((message, response))
    return history, history

with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Healthcare Multi-Agent AI System")
    gr.Markdown("AI-powered symptom analysis with RAG and safety guardrails.")

    chatbot = gr.Chatbot(height=400)
    msg = gr.Textbox(placeholder="Enter your symptoms...")
    clear = gr.Button("Clear Chat")

    msg.submit(chat_fn, [msg, chatbot], [chatbot, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()
