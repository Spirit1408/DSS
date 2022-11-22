"""Игра "Угадай число" версия 2
Компьютер сам загадывает число, которое должен отгадать
"""

import numpy as np


def predict_number(number: int=1) -> int:
    """Угадываем число

    Args:
        number (int, optional): Искомое число. По умолчанию 1.

    Returns:
        int: count - количество попыток
    """
    count = 0
    
    while True:
        predict_number = np.random.randint(1, 101)
        count += 1
        if predict_number == number:
            break
        
    return count

def game_score(predict_number) -> int:
    """Подсчет среднего количества попыток при отгадывании чисел от 1 до 100 1000 раз

    Args:
        predict_number (_type_): В качестве аргумента принимается функция угадывания числа

    Returns:
        int: score - среднее количество попыток угадывания числа
    """
    count_res = []
    np.random.seed(1)
    numbers_array = np.random.randint(1, 101, size=1000)
    
    for number in numbers_array:
        count_res.append(predict_number(number))
        
    score = int(np.mean(numbers_array))
    
    print(f"Числа были угаданы в среднем за {score} попыток. \n")
    return score

if __name__ == "__main__":
    game_score(predict_number)