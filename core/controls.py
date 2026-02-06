
from abc import ABC, abstractmethod


class VolumeControl(ABC):
    """Docstring для VolumeControl"""

    @abstractmethod
    async def set_volume(self, volume_level: int) -> None:
        pass

    @abstractmethod
    async def increase_volume(self, increment: int) -> None:
        pass

    @abstractmethod
    async def decrease_volume(self, decrement: int) -> None:
        pass


class BrightnessControl(ABC):
    """Docstring для BrightnessControl"""

    @abstractmethod
    async def set_brightness(self, brightness_level: int) -> None:
        pass

    @abstractmethod
    async def increase_brightness(self, increment: int) -> None:
        pass

    @abstractmethod
    async def decrease_brightness(self, decrement: int) -> None:
        pass


class TemperatureControl(ABC):
    """Docstring для TemperatureControl"""

    @abstractmethod
    async def set_temperature(self, temperature_level: int) -> None:
        pass

    @abstractmethod
    async def increase_temperature(self, increment: int) -> None:
        pass

    @abstractmethod
    async def decrease_temperature(self, decrement: int) -> None:
        pass


class HumidityControl(ABC):
    """Docstring для HumidityControl"""

    @abstractmethod
    async def set_humidity(self, humidity_level: int) -> None:
        pass

    @abstractmethod
    async def increase_humidity(self, increment: int) -> None:
        pass

    @abstractmethod
    async def decrease_humidity(self, decrement: int) -> None:
        pass


class CleaningModeSetup(ABC):
    """Docstring для CleaningModeSetup"""

    @abstractmethod
    def setup_clean_mode(self, clean_mode: str, power: int, pressure: int):
        pass


class AirQualityControl(ABC):
    """Docstring для AirQualityControl"""

    @abstractmethod
    async def set_air_quality(self, quality_level: int) -> None:
        pass

    @abstractmethod
    async def increase_air_quality(self, increment: int) -> None:
        pass

    @abstractmethod
    async def decrease_air_quality(self, decrement: int) -> None:
        pass
