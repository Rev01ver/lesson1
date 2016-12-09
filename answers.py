# def get_answer(k, d):
#     return d.get(k)
# dialog = {"Привет": "И тебе привет", "Как дела?": "Лучше всех", "Пока": "Увидимся"}
# key = input("Введите ключ ")
# print(get_answer(key.capitalize(), dialog))



answers = {"привет":"Привет!",
           "здарова":"здоровее видали",
           "как дела":"Нормально, не жалуюсь. Ты как?",
           "пока":"Ты это, заходи, если чё",
           "нормально":"Мой дедушка сказал бы тебе, что надо всегда говорить ""Хорошо""",
           "плохо":"У кого-то ещё хуже, держись",
           "хорошо":"Красавчег",
           "какой смысл жизни?":"ты далек от его понимания, если спрашиваешь у меня ;)",
           "купи слона":"купилка не выросла :("
            }

def get_answer(question,answers):
    return answers.get(question)

def ask_user(answers):
    while True:
        user_input = input("Скажи что-нибудь:")
        answer = get_answer(user_input,answers)
        if not answers.get(user_input):
             print("не понял тебя((")
        else:
            print(answer)

        if user_input == "пока":
            break
if __name__ == "__main__":
    ask_user(answers)

