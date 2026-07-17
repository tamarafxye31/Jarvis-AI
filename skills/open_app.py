import subprocess

from skills.base import BaseSkill
from engine.command_engine import CommandEngine


class OpenAppSkill(BaseSkill):

    APPS = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "cmd": "cmd.exe",
        "explorer": "explorer.exe",
    }

    def __init__(self):

        self.engine = CommandEngine()

    def can_handle(self, prompt):

        result = self.engine.resolve(
            prompt,
            self.APPS.keys()
        )

        return result is not None

    def execute(self, prompt):

        app = self.engine.resolve(
            prompt,
            self.APPS.keys()
        )

        if not app:
            return None

        subprocess.Popen(
            self.APPS[app]
        )

        return f"Opening {app}."