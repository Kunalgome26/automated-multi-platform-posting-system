
from abc import ABC, abstractmethod


class BasePlatform(ABC):

    @abstractmethod
    async def publish(self, message: str) -> dict:
        pass
