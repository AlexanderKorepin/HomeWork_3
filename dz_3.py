# from datetime import datetime
# import re
# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8
def zadacha_1():
    number = abs(int(input("Введите число N: ")))
    if number > 1:
        fibonachi = [1, 1]
        for i in range(2, number):
            fibonachi.append(fibonachi[-1] + fibonachi[-2])
    else:
        fibonachi = [1]
    print(f'Последовательность Фибоначи числа {number}:')
    print(*fibonachi)
# Задача 2. В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.
def zadacha_2():
    fruits = ["абрикос", "апельсин", "банан", "груша", "гранат","киви", "лимон", "мандарин", "манго", "персик","яблоко",]
    j = input("Введите букву: ").lower()[0]
    for i in fruits:
        if i[0] == j:
            print(i)
#Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
import re
def load_answer(filename):
    try:
        with open(filename) as file:
            content = file.read()
            return dict(line.split('\t') for line in content.split('\n') if line)
    except:
        return {
            "привет|здравствуй|здравствуйте": "Привет! Чем могу помочь?",
            "как тебя зовут": "Я чатбот.",
            "как дела": "Спасибо, хорошо!А у вас?",
            "Отлично!|Хорошо!": "Рад за вас!",
            "пока|досвидания!": "Всего доброго!Хорошего дня!",
            "error": "Извините, я не понимаю что вы хотели спросить. Пожалуйста, попробуйте задать вопрос по-другому."
            }
def save_answer(answer, filename):
    with open(filename, "w") as file:
        for key, value in answer.items():
            file.write(f"{key}\t{value}\n")
def find_response(phrase, answer):
    for key, value in answer.items():
        match = re.search(key, phrase, re.IGNORECASE)
        if match:
            return value.format(*match.groups())
    return answer["error"]
def bot_work(answer, filename):
    while True:
        user_input = input("Пользователь: ")
        if user_input.lower() == "выход":
            print("Чатбот: Всего доброго!")
            break
        reply = find_response(user_input, answer)
        if reply == answer["error"]:
            print("Чатбот:", reply)
            save_answer(answer, filename)
        else:
            print("Чатбот:", reply)
filename = "bot.txt"
answer = load_answer(filename)
bot_work(answer, filename)