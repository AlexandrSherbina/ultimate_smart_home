import asyncio
import random
from core import SwitchableDevice, Observer, BrightnessControl


class SmartLight(SwitchableDevice, Observer, BrightnessControl):
    """
    Docstring для SmartLight
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__brightness = 50

    def get_status(self) -> str:
        return f"{'Включена' if self._is_on else 'Выключена'}, яркость {self.__brightness}%"

    async def _perform_turn_on(self):
        print(f"[{self.name}] Подключение к серверу...")
        rand_time = random.randint(0, 2)
        await asyncio.sleep(rand_time)
        self._is_on = True
        print(f"[{self.name}] Лампа зажглась!")

    async def _perform_turn_off(self) -> None:
        self._is_on = False
        print('Лампа выключена')

    async def update(self, event_data: str) -> None:
        if event_data == "dark":
            await self._perform_turn_on()
        elif event_data == "light":
            await self._perform_turn_off()
