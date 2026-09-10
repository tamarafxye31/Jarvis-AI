import subprocess

from skills.base import BaseSkill


class HibernateSkill(BaseSkill):

    KEYWORDS = [
        "hibernate",
        "hibernate computer",
        "hibernate pc",
        "put computer into hibernation",
        "put pc into hibernation",
    ]

    def can_handle(self, prompt: str) -> bool:
        prompt = prompt.lower()
        return any(keyword in prompt for keyword in self.KEYWORDS)

    def execute(self, prompt: str):

        if not self.confirm(
            "Are you sure you want to hibernate the computer?"
        ):
            return "Hibernate cancelled."

        subprocess.run(
            ["shutdown", "/h", "/f"],
            check=True
        )

        return "Hibernating the computer..."