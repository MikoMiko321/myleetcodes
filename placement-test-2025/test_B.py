# Плагиат в Вышке крайне осуждается!

# Напишите функцию is_plagiat, которая принимает на вход два аргумента - строки word1 и word2 - и возвращает True,
# если слово является плагиатом, и False - если не является.

# word2 является плагиатом слова word1, если:

# Используются те же самые буквы либо есть еще одна дополнительная, которой нет в word1
# Регистр не имеет значения (слово "woRD" является плагиатом слова "word")
# Порядок не имеет значения - если буквы все совпадают (либо совпадают все, кроме одной),
# но расположены они в разном порядке - это все равно плагиат!
# Гарантируется, что слова состоят только из букв.


# Считайте две строки и выведите результат функции is_plagiat от них.
def is_plagiat(word1: str, word2: str) -> bool:
    word2 = set(word2.lower() + word1.lower())
    word1 = set(word1.lower())

    return (len(word2) - len(word1)) <= 1


word1 = input()
word2 = input()

print(is_plagiat(word1, word2))


def test_is_plagiat():
    assert is_plagiat("word", "owrd") == True, "Пример 1: переставлены буквы"
    assert (
        is_plagiat("word", "wordwordt") == True
    ), "Пример 2: одна лишняя буква, повторы не важны"
    assert is_plagiat("word", "wordtrue") == False, "Пример 3: две лишние буквы"
    assert (
        is_plagiat("word", "wo") == True
    ), "Пример 4: неполное совпадение, но не больше одной новой буквы"
    assert is_plagiat("word", "DRow") == True, "Пример 5: регистр не важен, буквы те же"
    assert is_plagiat("word", "WeLcOmE") == False, "Пример 6: почти ничего общего"

    print("✅ All 6 tests passed.")


test_is_plagiat()

word1, word2 = map(str, input().split())
