import json
import aiofiles
import os
from dotenv import load_dotenv

# Загружаем настройки из .env
load_dotenv()


class StateStorage:
    """
    Docstring для StateStorage
    Класс для асинхронного сохранения и загрузки состояния устройств в JSON файл.
    """

    def __init__(self):
        # Берем путь из .env, если его нет — используем значение по умолчанию
        self.file_path = os.getenv("STATE_FILE_PATH", "house_state.json")

    async def save_state(self, devices: list):
        """Асинхронно сохраняет состояние всех устройств в JSON."""
        data = []
        for device in devices:
            # Собираем данные (у каждого устройства должен быть get_status или to_dict)
            data.append({
                "name": device.name,
                "status": device.get_status(),
                "type": device.__class__.__name__
            })

        try:
            # Открываем файл асинхронно
            async with aiofiles.open(self.file_path, mode='w', encoding='utf-8') as f:
                # Превращаем список в красивую JSON-строку
                json_data = json.dumps(data, ensure_ascii=False, indent=4)
                # Записываем строку в файл
                await f.write(json_data)
            print(f"[STORAGE] Состояние успешно сохранено в {self.file_path}")
        except Exception as e:
            print(f"[STORAGE] Ошибка при сохранении: {e}")

    async def load_state(self):
        """Асинхронно читает состояние из файла."""
        if not os.path.exists(self.file_path):
            return []

        async with aiofiles.open(self.file_path, mode='r', encoding='utf-8') as f:
            content = await f.read()
            return json.loads(content)
