class Router:

    def __init__(self):
        self.skills = []

    def register(self, skill):
        self.skills.append(skill)

    def route(self, prompt: str):

        for skill in self.skills:

            if skill.can_handle(prompt):
                return skill.execute(prompt)

        return None