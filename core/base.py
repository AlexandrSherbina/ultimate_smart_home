from abc import ABC, abstractmethod
from decorators import log_action


class BaseDevice(ABC):
    """Docstring для BaseDevice"""

    def __init__(self, name: str) -> None:
        self.__name = name

    @abstractmethod
    def get_status(self) -> str:
        pass

    @property
    def name(self):
        return self.__name


class SwitchableDevice(BaseDevice):
    """
    Docstring для SwitchableDevice
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._is_on = False

    @log_action
    async def turn_on(self) -> None:
        # Этот метод больше никто не переопределяет!
        # Он вызывает внутренний метод, который сделают дети
        await self._perform_turn_on()

    @abstractmethod
    async def _perform_turn_on(self):
        pass

    @log_action
    async def turn_off(self) -> None:
        await self._perform_turn_off()

    @abstractmethod
    async def _perform_turn_off(self) -> None:
        pass
