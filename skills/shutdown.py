import subprocess

from skills.base import BaseSkill


class ShutdownSkill(BaseSkill):

    KEYWORDS = [
        "shutdown",
        "shut down",
        "turn off",
        "power off",
    ]

    def can_handle(self, prompt: str) -> bool:
        prompt = prompt.lower()
        return any(keyword in prompt for keyword in self.KEYWORDS)

    def execute(self, prompt: str):

        confirmation = input(
            "Are you sure you want to shut down the computer? (y/n): "
        ).strip().lower()

        if confirmation != "y":
            return "Shutdown cancelled."

        subprocess.run(
            ["shutdown", "/s", "/t", "0"],
            check=True
        )

        return "Shutting down the computer..."