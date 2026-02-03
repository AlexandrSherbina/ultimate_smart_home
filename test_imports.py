try:
    import aiofiles
    import dotenv
    print("✅ Ура! Все библиотеки на месте и видны проекту.")
except ImportError as e:
    print(f"❌ Ошибка: {e}. Проверь настройки интерпретатора!")
