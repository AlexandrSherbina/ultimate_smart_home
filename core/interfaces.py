# ABC interfaces here

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Docstring для Observer
    """
    @abstractmethod
    async def update(self, event_data: str) -> None:
        pass


class MusicPlayer(ABC):
    """Docstring для MusicPlayer"""
    @abstractmethod
    async def play_music(self, track_name: str) -> None:
        pass

    @abstractmethod
    async def stop_music(self, track_name: str) -> None:
        pass

    @abstractmethod
    async def pause_music(self, track_name: str) -> None:
        pass


class Cleaner(ABC):
    """Docstring для Cleaner"""

    @abstractmethod
    async def start_cleaning(self) -> None:
        pass

    @abstractmethod
    async def stop_cleaning(self) -> None:
        pass

    @abstractmethod
    def setup_clean_mode(self, clean_mode: str, power: int, pressure: int):
        pass
