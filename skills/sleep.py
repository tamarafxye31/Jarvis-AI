import subprocess

from skills.base import BaseSkill


class SleepSkill(BaseSkill):

    KEYWORDS = [
        "sleep",
        "sleep computer",
        "sleep pc",
        "put computer to sleep",
        "put pc to sleep",
    ]

    def can_handle(self, prompt: str) -> bool:
        prompt = prompt.lower()
        return any(keyword in prompt for keyword in self.KEYWORDS)

    def execute(self, prompt: str):

        if not self.confirm(
            "Are you sure you want to put the computer to sleep?"
        ):
            return "Sleep cancelled."

        subprocess.run(
            [
                "powershell",
                "-Command",
                "Add-Type -AssemblyName System.Windows.Forms; "
                "[System.Windows.Forms.Application]::SetSuspendState("
                "'Suspend', $false, $false)"
            ],
            check=True
        )

        return "Putting the computer to sleep..."