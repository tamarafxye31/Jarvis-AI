from assistant.llm import LLM, SYSTEM_PROMPT
from assistant.memory import Memory
from engine.skill_manager import SkillManager


class Assistant:

    def __init__(self):
        self.memory = Memory()
        self.llm = LLM()
        self.skill_manager = SkillManager()

        self.memory.add(
            "system",
            SYSTEM_PROMPT
        )

    def chat(self, prompt: str):

        skill = self.skill_manager.find_skill(prompt)

        if skill:
            return skill.execute(prompt)

        self.memory.add(
            "user",
            prompt
        )

        response = self.llm.ask(
            self.memory.get()
        )

        self.memory.add(
            "assistant",
            response
        )

        return response