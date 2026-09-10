import subprocess

from skills.base import BaseSkill


class LockSkill(BaseSkill):

    KEYWORDS = [
        "lock",
        "lock computer",
        "lock pc",
        "lock my computer",
        "lock my pc",
    ]

    def can_handle(self, prompt: str) -> bool:
        prompt = prompt.lower()
        return any(keyword in prompt for keyword in self.KEYWORDS)

    def execute(self, prompt: str):

        if not self.confirm(
            "Are you sure you want to lock the computer?"
        ):
            return "Lock cancelled."

        subprocess.run(
            ["rundll32.exe", "user32.dll,LockWorkStation"],
            check=True
        )

        return "Locking the computer..."