"""Программа для угадывания числа и определения
среднего количества попыток для его определения.
"""

import numpy as np

def random_predict(number:int=1) -> int: #Указываем, что тип ввода и вывода будет int.
    """Нахождение числа, заданного произвольно

    Args: 
        number (int, optional): Загаданное число. По умолчанию 1.

    Returns:
        int: count - количество попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    # print(f'Алгоритм угадывает число {number} за {count} попыток')
    return count

def score_game(random_predict) -> int:
    """Программа для определения среднего количества попыток угадывания числа

    Args:
        random_predict (_type_): На вход принимает результат предыдущей функции

    Returns:
        int: score - среднее количество попыток
    """
    
    count_ls = [] # Список для количества попыток для каждого числа
    np.random.seed(1) # Заморозка зерна генерации, для воспроизводимости результата
    random_array = np.random.randint(1,101,size=1000) # Генерация чисел от 1 до 100, в размере 1000 элементов.
    
    for number in random_array:
        count_ls.append(random_predict(number)) # Для каждого числа из генерации - с помощью функции 
        # random_predict высчитывается количество попыток и заносится в список count_ls.
    
    score = int(np.mean(count_ls)) # Высчитываем среднее значение списка count_ls
    print()
    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    print()
    return score
# RUN
if __name__ == '__main__':
    score_game(random_predict)