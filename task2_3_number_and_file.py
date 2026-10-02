"""Завдання 2 і 3: обробка винятків при введенні числа та читанні файлу."""


def task2_convert_number() -> None:
    """Запитує число, конвертує в ціле, обробляє ValueError."""
    value = input("Введіть число: ")
    try:
        number = int(value)
    except ValueError:
        print(f"Помилка: '{value}' не можна перетворити на ціле число.")
    else:
        print(f"Ціле число: {number}")


def task3_read_file() -> None:
    """Зчитує файл за шляхом і виводить вміст, обробляє відсутній файл."""
    path = input("Введіть шлях до файлу: ").strip()
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не існує.")
    except IsADirectoryError:
        print(f"Помилка: '{path}' є папкою, а не файлом.")
    except PermissionError:
        print(f"Помилка: немає доступу до файлу '{path}'.")
    except UnicodeDecodeError:
        print(f"Помилка: файл '{path}' не є текстовим UTF-8.")
    else:
        print("--- Вміст файлу ---")
        print(content)


def main() -> None:
    print("=== Завдання 2 ===")
    task2_convert_number()
    print("\n=== Завдання 3 ===")
    task3_read_file()


if __name__ == "__main__":
    main()
