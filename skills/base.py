from abc import ABC, abstractmethod


class BaseSkill(ABC):

    def confirm(self, message: str) -> bool:
        confirmation = input(f"{message} (y/n): ").strip().lower()
        return confirmation == "y"

    @abstractmethod
    def can_handle(self, prompt: str):
        pass

    @abstractmethod
    def execute(self, prompt: str):
        pass