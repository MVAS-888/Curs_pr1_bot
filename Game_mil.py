import random

# База запитань і відповідей
questions = [
    {
        "question": "Яка столиця України?",
        "options": ["Київ", "Львів", "Одеса", "Харків"],
        "answer": "Київ"
    },
    {
        "question": "Який результат 7 * 8?",
        "options": ["54", "56", "49", "64"],
        "answer": "56"
    },
    {
        "question": "Хто є автором роману '1984'?",
        "options": ["Джордж Оруелл", "Марк Твен", "Френсіс Скотт Фіцджеральд", "Джейн Остін"],
        "answer": "Джордж Оруелл"
    },
    {
        "question": "Скільки планет у Сонячній системі?",
        "options": ["7", "8", "9", "10"],
        "answer": "8"
    },
    {
        "question": "Яка хімічна формула води?",
        "options": ["H2O", "CO2", "NaCl", "O2"],
        "answer": "H2O"
    }
]

# Налаштування гри
prizes = [100, 200, 300, 500, 1000]  # Призи за кожне питання
used_hints = {"50/50": False, "Дзвінок другу": False, "Допомога залу": False}

# Функції підказок
def use_50_50(question):
    """
    Реалізує підказку 50/50, видаляючи два неправильних варіанти.
    """
    options = question["options"]
    correct_answer = question["answer"]
    wrong_answers = [opt for opt in options if opt != correct_answer]
    random.shuffle(wrong_answers)
    hint_options = [correct_answer, wrong_answers[0]]
    random.shuffle(hint_options)
    return hint_options


def call_a_friend(question):
    """
    Реалізує підказку 'Дзвінок другу'.
    """
    options = question["options"]
    return random.choice(options)


def audience_help(question):
    """
    Реалізує підказку 'Допомога залу'.
    """
    options = question["options"]
    correct_answer = question["answer"]
    percentages = {opt: random.randint(1, 100) for opt in options}
    percentages[correct_answer] += random.randint(10, 20)  # Збільшення шансів для правильної відповіді
    total = sum(percentages.values())
    percentages = {opt: int((percent / total) * 100) for opt, percent in percentages.items()}
    return percentages

# Основна функція гри
def millionaire_game():
    print("Вітаємо у грі 'Хто хоче стати мільйонером!'")
    print("Відповідайте на питання та вигравайте гроші!\n")

    current_prize = 0

    for i, question in enumerate(questions):
        print(f"\nПитання {i + 1} на {prizes[i]} гривень:")
        print(question["question"])
        for idx, option in enumerate(question["options"], 1):
            print(f"{idx}. {option}")

        # Підказки
        print("\nПідказки: 50/50, Дзвінок другу, Допомога залу")
        print("Щоб використати підказку, введіть її назву (або просто натисніть Enter для пропуску).")
        hint = input("Ваш вибір підказки: ").strip().lower()

        if hint == "50/50" and not used_hints["50/50"]:
            used_hints["50/50"] = True
            hint_options = use_50_50(question)
            print(f"Варіанти після підказки: {', '.join(hint_options)}")
        elif hint == "дзвінок другу" and not used_hints["Дзвінок другу"]:
            used_hints["Дзвінок другу"] = True
            friend_answer = call_a_friend(question)
            print(f"Друг каже, що це: {friend_answer}")
        elif hint == "допомога залу" and not used_hints["Допомога залу"]:
            used_hints["Допомога залу"] = True
            audience = audience_help(question)
            print("Голосування залу:")
            for option, percentage in audience.items():
                print(f"{option}: {percentage}%")
        elif hint:
            print("Підказка вже використана або не існує!")

        # Відповідь гравця
        answer = input("\nВаш варіант відповіді (1-4): ").strip()
        try:
            answer = int(answer)
            if question["options"][answer - 1] == question["answer"]:
                print("Правильно!")
                current_prize += prizes[i]
            else:
                print("Неправильно! Ви програли.")
                break
        except (IndexError, ValueError):
            print("Невірний формат відповіді. Ви програли.")
            break

    print(f"\nГра завершена! Ви виграли {current_prize} гривень.")

# Запуск гри
if __name__ == "__main__":
    millionaire_game()
