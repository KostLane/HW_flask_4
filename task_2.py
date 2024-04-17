import random
import time
import threading

def sum_elements(start, end, result):
    result.append(sum(arr[start:end]))

arr = [random.randint(1, 100) for _ in range(1000000)]
result = []
start_time = time.time()

threads = []
for i in range(10):
    t = threading.Thread(target=sum_elements, args=(i*100000, (i+1)*100000, result))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

total_sum = sum(result)
print(f"Общая сумма: {total_sum}")
print(f"Время выполнения: {time.time() - start_time}")
