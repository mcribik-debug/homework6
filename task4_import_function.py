"""Завдання 4: імпорт модуля та безпечний виклик функції з нього."""

import importlib


def call_function(module_name: str, func_name: str, *args):
    """Імпортує модуль і викликає функцію, обробляючи типові помилки."""
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        print(f"Помилка: модуль '{module_name}' не знайдено.")
        return None

    try:
        func = getattr(module, func_name)
    except AttributeError:
        print(f"Помилка: у модулі '{module_name}' немає функції '{func_name}'.")
        return None

    if not callable(func):
        print(f"Помилка: '{func_name}' не є функцією.")
        return None

    try:
        return func(*args)
    except TypeError as error:
        print(f"Помилка виклику '{func_name}': {error}")
        return None


def main() -> None:
    module_name = input("Назва модуля (наприклад, math): ").strip()
    func_name = input("Назва функції (наприклад, sqrt): ").strip()
    raw_arg = input("Аргумент-число (або Enter, якщо без аргументів): ").strip()

    args = ()
    if raw_arg:
        try:
            args = (float(raw_arg),)
        except ValueError:
            print("Аргумент має бути числом.")
            return

    result = call_function(module_name, func_name, *args)
    if result is not None:
        print(f"Результат: {result}")


if __name__ == "__main__":
    main()
