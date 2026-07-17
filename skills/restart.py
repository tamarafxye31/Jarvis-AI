import subprocess

from skills.base import BaseSkill


class RestartSkill(BaseSkill):

    KEYWORDS = [
        "restart",
        "reboot",
        "restart computer",
        "restart pc",
    ]

    def can_handle(self, prompt: str) -> bool:
        prompt = prompt.lower()
        return any(keyword in prompt for keyword in self.KEYWORDS)

    def execute(self, prompt: str):
        if not self.confirm("Are you sure you want to restart the computer?"):
            return "Restart cancelled."

        subprocess.run(
            ["shutdown", "/r", "/t", "0"],
            check=True
        )

        return "Restarting the computer..."