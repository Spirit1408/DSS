"""Игра "Угадай число"
Компьютер загадывает число, которое должен отгадать пользователь
"""

import numpy as np

count = 0 # Переменная - счетчик

number = np.random.randint(1,101)

while True:
    # Цикл принимает число и сравнивает с заданным
    # Если выполняется одно из условий неравенства - на экран возвращается подсказка
    # Работа цикла прерывается, когда не выполняется ни одно из условий неравенств
    predict_number = int(input("Введите число: ")) # Переменная принимает число с клавиатуры
    count += 1
    if predict_number > number:
        print("Введенное число больше искомого \n")
    elif predict_number < number:
        print("Введенное число меньше искомого \n")
    else:
        print(f"Поздравляем! Вы угадали число {number} за {count} попыток! \n")
        break # Завершение цикла для сверки чисел