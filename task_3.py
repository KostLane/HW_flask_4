import random
import time
from multiprocessing import Process, Queue

def sum_elements(start, end, queue):
    queue.put(sum(arr[start:end]))

arr = [random.randint(1, 100) for _ in range(1000000)]
queue = Queue()
    
if __name__ == '__main__':
    processes = []
    start_time = time.time()

    for i in range(10):
        p = Process(target=sum_elements, args=(i*100000, (i+1)*100000, queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    total_sum = sum(queue.get() for _ in range(10))
    print(f"Общая сумма: {total_sum}")
    print(f"Время выполнения: {time.time() - start_time}")
