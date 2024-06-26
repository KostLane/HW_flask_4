# Задание №7
#  Напишите программу на Python, которая будет находить 
# сумму элементов массива из 1000000 целых чисел. 
#  Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
#  Массив должен быть заполнен случайными целыми числами 
# от 1 до 100.
#  При решении задачи нужно использовать многопоточность, 
# многопроцессорность и асинхронность. 
#  В каждом решении нужно вывести время выполнения 
# вычислений.

import random
import time

def create_lists():
    lists = []
    for _ in range(10):
        list_ = [random.randint(1, 100) for _ in range(100_000)]
        lists.append(list_)
    return lists
start_time = time.time()

def total_sum(lists):
    total = 0
    for list_ in lists:
        total += sum(list_)
    return total


lists = create_lists()

total = total_sum(lists)

print(f"Общая сумма элементов всех списков: {total}")
print(f"Время выполнения: {time.time() - start_time}")
