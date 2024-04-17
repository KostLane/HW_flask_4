import random
import time
import asyncio

async def sum_elements(start, end):
    return sum(arr[start:end])

arr = [random.randint(1, 100) for _ in range(1000000)]
start_time = time.time()

loop = asyncio.get_event_loop()
tasks = [loop.create_task(sum_elements(i*100000, (i+1)*100000)) for i in range(10)]
total_sum = sum(loop.run_until_complete(asyncio.gather(*tasks)))
print(f"Общая сумма: {total_sum}")
print(f"Время выполнения: {time.time() - start_time}")
