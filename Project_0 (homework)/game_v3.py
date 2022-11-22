"""Игра "Угадай число" версия 3
Компьютер сам загадывает число, которое должен отгадать.
Модификация программы для отгадывания не более чем за 20 попыток.
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
    min = 1
    max = 100 
    number = np.random.randint(min, max) # Генерируем произвольное число
    word = ""
    
    while True:
        """В цикле определяем средину диапазона поиска.
        Если искомое число больше или меньше середины - 
        диапазон поиска сокращается до (или от) середины, в зависимости от условия.
        """
        count += 1        
        mid = int((max+min) / 2)
        
        if mid > number:
            max = mid
        elif mid < number:
            min = mid
        else:
            break
            
    if count == 1:
        word = "попытку"
    elif count in range(2,5):
        word = "попытки"
    elif count > 4:
        word = "попыток"
        
    print(f"Число {number} было угадано за {count} {word}.")                      
    return count

    
def game_score(predict_number) -> int:
    """Производим определение числа 1000 раз,
    а также подсчитываем среднее значение попыток

    Args:
        predict_number (_type_): В качестве аргумента принимается результат функции predict_number
    Returns:
        int: score - среднее колчество попыток
    """
    res_list = [] # Переменная для списка количества попыток для каждого заданного числа
    array_num = np.random.randint(1,101, size=1000) # Генерируем 1000 чисел в диапазоне от 1 до 100
    
    for num in array_num:
        """ Вычисление количества попыток для каждого числа,
        с последующим занесением в список
        """
        res_list.append(predict_number(num))
        
    score = int(np.mean(res_list)) # Вычисление среднего количества попыток
    
    print(f"\nСреднее количество попыток на 1000 чисел: {score}")

if __name__ == "__main__":
    game_score(predict_number)