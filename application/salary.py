from tqdm import tqdm
from time import sleep


def calculate_salary():
    print(f'Идёт расчет зарплаты функцией calculate_salary в модуле {__name__}')
    for _ in tqdm(range(100)):
        sleep(0.1)
