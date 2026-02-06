import asyncio
from core import SwitchableDevice, MusicPlayer, VolumeControl, Observer, log_action


class SmartSpeaker(SwitchableDevice, MusicPlayer, VolumeControl, Observer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._volume = 50
        self._current_track = None

    def get_status(self) -> str:
        state = "ВКЛ" if self._is_on else "ВЫКЛ"
        return f"{state}, Громкость: {self._volume}%, Трек: {self._current_track}"

    # Реализация SwitchableDevice
    async def _perform_turn_on(self):
        await asyncio.sleep(0.5)  # Имитация загрузки системы
        print(f"[{self.name}] Привет! Я готова играть музыку.")

    async def _perform_turn_off(self):
        self._current_track = None
        print(f"[{self.name}] Пока! Отключаюсь...")

    # Реализация MusicPlayer
    @log_action
    async def play_music(self, track_name: str):
        if self._is_on:
            self._current_track = track_name
            print(f"[{self.name}] Играет: {track_name}")

    @log_action
    async def stop_music(self, track_name: str):
        if self._is_on and self._current_track == track_name:
            print(f"[{self.name}] Останавливаю: {track_name}")
            self._current_track = None

    @log_action
    async def pause_music(self, track_name: str):
        if self._is_on and self._current_track == track_name:
            print(f"[{self.name}] Пауза: {track_name}")

    # Реализация VolumeControl
    @log_action
    async def increase_volume(self, increment: int) -> None:
        if self._is_on:
            self._volume = min(100, self._volume + increment)
            print(f"[{self.name}] Громкость увеличена до {self._volume}%")

    @log_action
    async def decrease_volume(self, decrement: int) -> None:
        if self._is_on:
            self._volume = max(0, self._volume - decrement)
            print(f"[{self.name}] Громкость уменьшена до {self._volume}%")

    @log_action
    async def set_volume(self, volume_level: int) -> None:
        self._volume = max(0, min(100, volume_level))
        if self._is_on:
            print(f"[{self.name}] Громкость установлена на {self._volume}%")

    # Реализация Observer (реакция на события)
    async def update(self, event_data: str):
        if "FIRE" in event_data:
            print(
                f"[{self.name}] 🚨 ВНИМАНИЕ! Обнаружено задымление! Включаю сирену!")
            self._volume = 100
            await self.play_music("СИРЕНА_ПОЖАРНАЯ.mp3")
