import numpy as np
def random_predict(number:int=1) -> int:
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    print(f"Число {predict_number}. Кол-во попыток – {count}")
random_predict(5)