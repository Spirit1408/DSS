"""[Угадываем число, написанным с клавиатуры]
"""
import numpy as np

number = np.random.randint(1,101)
count=0

while True:
    count += 1
    predict_number = int(input("Введите число от 1 до 100: "))
    if predict_number>number:
        print(f"Число должно быть меньше чем {predict_number}")
    elif predict_number<number:
        print(f"Число должно быть больше чем {predict_number}")
    else:
        print(f"Вы угадали число! Это число {number}, угаданное за {count} попыток")
        break