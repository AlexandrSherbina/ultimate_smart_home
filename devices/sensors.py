from core import BaseDevice, log_action
import asyncio


class SmokeSensor(BaseDevice):
    def __init__(self, name: str):
        super().__init__(name)
        self._observers = []

    def get_status(self) -> str:
        return "Датчик активен"

    def attach(self, observer):
        self._observers.append(observer)

    @log_action
    async def trigger(self):
        """Имитация срабатывания датчика."""
        print(
            f"\a[{self.name}] !!! ДЫМ ОБНАРУЖЕН !!!")  # \a — звуковой сигнал в некоторых терминалах
        # Оповещаем всех подписчиков асинхронно
        tasks = [obs.update("FIRE") for obs in self._observers]
        await asyncio.gather(*tasks)
