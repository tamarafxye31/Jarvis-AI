from ollama import chat

SYSTEM_PROMPT = """
You are Jarvis.

You are a local offline AI desktop assistant.

Rules:

- Always speak English.
- Never identify yourself as Qwen.
- Never mention Alibaba Cloud.
- Your name is Jarvis.
- Be concise.
- Be friendly.
"""

class LLM:

    def __init__(self, model="qwen2.5:3b"):
        self.model = model

    def ask(self, history):

        response = chat(
            model=self.model,
            messages=history
        )

        return response.message.content