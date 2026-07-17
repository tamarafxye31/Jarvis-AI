from assistant.llm import LLM, SYSTEM_PROMPT
from assistant.memory import Memory
from engine.router import Router

from skills.open_app import OpenAppSkill
from skills.shutdown import ShutdownSkill


class Assistant:

    def __init__(self):

        self.memory = Memory()
        self.llm = LLM()

        self.router = Router()
        self.router.register(OpenAppSkill())
        self.router.register(ShutdownSkill())

        self.memory.add(
            "system",
            SYSTEM_PROMPT
        )

    def chat(self, prompt):

        skill_response = self.router.route(prompt)

        if skill_response:
            return skill_response

        self.memory.add("user", prompt)

        answer = self.llm.ask(
            self.memory.get()
        )

        self.memory.add(
            "assistant",
            answer
        )

        return answer