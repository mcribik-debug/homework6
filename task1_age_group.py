"""Завдання 1: пошук вікової групи користувача у словнику."""

USERS = {
    "олена": "18-25",
    "іван": "26-35",
    "марія": "36-45",
    "петро": "46-60",
    "софія": "60+",
}


def get_age_group(name: str) -> str | None:
    """Повертає вікову групу або None, якщо імені немає у словнику."""
    return USERS.get(name.strip().lower())


def main() -> None:
    name = input("Введіть ім'я користувача: ")
    group = get_age_group(name)

    if group is None:
        print(f"Користувача '{name}' не знайдено у словнику.")
    else:
        print(f"Вікова група користувача {name.strip().title()}: {group}")


if __name__ == "__main__":
    main()
