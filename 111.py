import random
import string


def generate_random_word(length=5):
    # Определяем набор символов, из которых будут состоять слова
    characters = string.ascii_letters  # Все буквы английского алфавита (как заглавные, так и строчные)

    # Генерируем случайное слово
    random_word = ''.join(random.choice(characters) for _ in range(length))

    return random_word


def word_eng(myword):
    vowels = "aeiou"
    anti_vowels = "bcdfghjklmnpqrstvwxyz"

    first_letter = myword[0].lower()

    if first_letter in vowels:
        myword += "ay"
    elif first_letter in anti_vowels:
        myword = myword[1:] + myword[0] + "ay"

    return myword


# Пример использования
random_word = generate_random_word(5)
print(f"Случайное слово: {random_word}")
print(f"Преобразованное слово: {word_eng(random_word)}")

