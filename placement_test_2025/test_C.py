# Создайте декоратор log_plagiat_check, который будет использоваться для функции is_plagiat из предыдущей задачи.
# Этот декоратор должен выводить на экран информацию о том, какие слова проверяются и какой результат проверки.

# Решение обязательно должно содержать:

# код декоратора log_plagiat_check
# код функции is_plagiat
# чтение входных данных и применение функции is_plagiat
# Входные данные необходимо считать из файла "words.txt". Файл содержит неизвестное число строк.
# Каждая строка содержит два слова через пробел. Необходимо для каждой строки вывести на экран:

# оба слова
# результат действия функции is_plagiat
# Формат ввода
# Файл words.txt.

# Файл содержит неизвестное число строк. Каждая строка содержит два слова через пробел.

# Формат вывода
# Строка формата "Check '{слово1}' vs '{слово2}' -> {True/False}"


def log_plagiat_check(func):
    def wrapper(word1, word2):
        result = func(word1, word2)
        print(f"Check '{word1}' vs '{word2}' -> {result}")
        return result

    return wrapper


@log_plagiat_check
def is_plagiat(word1: str, word2: str) -> bool:
    word2 = set(word2.lower() + word1.lower())
    word1 = set(word1.lower())
    return (len(word2) - len(word1)) <= 1


with open("./placement-test-2025/words.txt", "r", encoding="utf-8") as file:
    lines = file.read().splitlines()

for line in lines:
    word1, word2 = map(str, line.split())
    is_plagiat(word1, word2)
