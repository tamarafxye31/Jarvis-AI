from abc import ABC, abstractmethod


class BaseSkill(ABC):

    @abstractmethod
    def can_handle(self, prompt: str):
        pass

    @abstractmethod
    def execute(self, prompt: str):
        pass