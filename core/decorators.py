import functools
from datetime import datetime


def log_action(func):
    @functools.wraps(func)  # Сохраняет имя и описание исходной функции
    async def wrapper(self, *args, **kwargs):
        current_time = datetime.now()
        format_time = current_time.strftime("%H:%M:%S")
        print(
            f"[{format_time}] [LOG] Выполняется действие: <{func.__name__}>, на устройстве <{self.name}>")
        result = await func(self, *args, **kwargs)
        return result
    return wrapper
