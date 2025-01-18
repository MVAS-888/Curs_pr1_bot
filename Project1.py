import random
import pyjokes
import emoji
from art import text2art
from prettytable import PrettyTable
from colorama import Fore, Style

# Головне меню


def main_menu():
    print(Fore.CYAN + "\nГоловне меню:")
    print("1. Рекомендації")
    print("2. Анекдоти")
    print("3. Ігри")
    print("4. Вийти" + Style.RESET_ALL)
    return input(Fore.YELLOW + "Оберіть опцію: " + Style.RESET_ALL).strip()

# Функція рекомендацій


def recommendations():
    genres = ["Фільми", "Музика", "Ігри"]
    print(Fore.GREEN + "\nОберіть жанр:" + Style.RESET_ALL)
    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre}")
    choice = input(Fore.YELLOW + "Ваш вибір: " + Style.RESET_ALL).strip()

    if choice == "1":
        print(Fore.BLUE + "\nРекомендовані фільми:" + Style.RESET_ALL)
        print("1. Inception\n2. Interstellar\n3. The Matrix")
    elif choice == "2":
        print(Fore.BLUE + "\nРекомендована музика:" + Style.RESET_ALL)
        print(
            "1. Queen - Bohemian Rhapsody\n2. Imagine Dragons - Believer\n3. BTS - Dynamite")
    elif choice == "3":
        print(Fore.BLUE + "\nРекомендовані ігри:" + Style.RESET_ALL)
        print("1. The Legend of Zelda\n2. Minecraft\n3. The Witcher 3")

# Функція анекдотів


def jokes():
    print(Fore.MAGENTA + "\nАнекдот дня:" + Style.RESET_ALL)
    print(pyjokes.get_joke(language="en", category="neutral"))

# Ігрове меню


def games_menu():
    print(Fore.CYAN + "\nІгри:")
    print("1. Камінь-ножиці-папір")
    print("2. Вгадай число")
    print("3. Поле чудес")
    print("4. Назад" + Style.RESET_ALL)
    return input(Fore.YELLOW + "Оберіть гру: " + Style.RESET_ALL).strip()

# Гра: Камінь-ножиці-папір


def rock_paper_scissors():
    options = ["камінь", "ножиці", "папір"]
    user_choice = input(
        Fore.YELLOW + "Оберіть: камінь, ножиці або папір: " + Style.RESET_ALL).lower()
    bot_choice = random.choice(options)
    print(Fore.BLUE + f"Бот обрав: {bot_choice}" + Style.RESET_ALL)

    if user_choice == bot_choice:
        print(Fore.GREEN + "Нічия!" + Style.RESET_ALL)
    elif (user_choice == "камінь" and bot_choice == "ножиці") or \
         (user_choice == "ножиці" and bot_choice == "папір") or \
         (user_choice == "папір" and bot_choice == "камінь"):
        print(Fore.GREEN + "Ви виграли!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Бот виграв!" + Style.RESET_ALL)

# Гра: Вгадай число


def guess_the_number():
    number = random.randint(1, 10)
    print(Fore.CYAN + "\nЯ загадав число від 1 до 10. Спробуйте вгадати." + Style.RESET_ALL)
    attempts = 0
    while True:
        guess = int(input(Fore.YELLOW + "Ваше число: " + Style.RESET_ALL))
        attempts += 1
        if guess == number:
            print(
                Fore.GREEN + f"Ви вгадали! Це було число {number}. Спроб {attempts}." + Style.RESET_ALL)
            break
        elif guess < number:
            print(Fore.RED + "Занадто мало!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Занадто багато!" + Style.RESET_ALL)

# Головна функція


def main():
    print(Fore.CYAN + text2art("Chat Bot") + Style.RESET_ALL)
    while True:
        choice = main_menu()
        if choice == "1":
            recommendations()
        elif choice == "2":
            jokes()
        elif choice == "3":
            while True:
                game_choice = games_menu()
                if game_choice == "1":
                    rock_paper_scissors()
                elif game_choice == "2":
                    guess_the_number()
                elif game_choice == "4":
                    break
                else:
                    print(Fore.RED + "Невірний вибір." + Style.RESET_ALL)
        elif choice == "4":
            print(Fore.GREEN + "Дякую за гру! До побачення!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Невірний вибір. Спробуйте ще раз." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
