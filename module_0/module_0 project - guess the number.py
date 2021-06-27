import numpy as np


def game_core_v3(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного.
    Функция принимает загаданное число и возвращает число попыток

    Андрей Шацев: Функция для "угадывания" модифицировна следующим образом:
     для угадывания числа накладывает несколько дополнительных условий. Первое условие начинает перебор значений
    близко к концу диапазона (близко к 100), второе условие - к середине диапазона и третье условие близко
    к началу диапазона (оно было по умолчанию).
    Далее были подобраны оптимально параметры шагов перебора в каждой из трех функций, обеспечивающие решение задачи
    за 4 попытки."""

    count = 1
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1

        # условие старта перебора значений близкое к конце диапазона (к 100)
        if number + 75 > predict:
            if number > predict:
                predict += 10
            elif number < predict:
                predict -= 8

        # условие старта перебора значений близкое к середине диапазона (к 50)
        if number + 50 > predict:
            if number > predict:
                predict += 5
            elif number < predict:
                predict -= 4

        # условие близкое к началу диапазона (было по default)
        if number > predict:
            predict += 2
        elif number < predict:
            predict -= 1

    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем
score_game(game_core_v3)
