from skills.open_app import OpenAppSkill
from skills.shutdown import ShutdownSkill
from skills.restart import RestartSkill
from skills.sleep import SleepSkill
from skills.hibernate import HibernateSkill
from skills.lock import LockSkill


class SkillManager:

    def __init__(self):
        self.skills = []

        self.register(OpenAppSkill())
        self.register(ShutdownSkill())
        self.register(RestartSkill())
        self.register(SleepSkill())
        self.register(HibernateSkill())
        self.register(LockSkill())

    def register(self, skill):
        self.skills.append(skill)

    def find_skill(self, prompt: str):
        for skill in self.skills:
            if skill.can_handle(prompt):
                return skill

        return None