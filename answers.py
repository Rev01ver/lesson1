def get_answer(k, d):
    return d.get(k)
dialog = {"Привет": "И тебе привет", "Как дела?": "Лучше всех", "Пока": "Увидимся"}
key = input("Введите ключ ")
print(get_answer(key.capitalize(), dialog))