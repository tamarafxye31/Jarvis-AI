from core.llm import LLM, SYSTEM_PROMPT
from core.memory import Memory


class Assistant:

    def __init__(self):

        self.memory = Memory()
        self.llm = LLM()

        self.memory.add(
            "system",
            SYSTEM_PROMPT
        )

    def chat(self, prompt):

        self.memory.add(
            "user",
            prompt
        )

        answer = self.llm.ask(
            self.memory.get()
        )

        self.memory.add(
            "assistant",
            answer
        )

        return answer