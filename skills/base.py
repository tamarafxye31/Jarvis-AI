class Skill:

    def can_handle(self, prompt: str) -> bool:
        return False

    def execute(self, prompt: str):
        return None