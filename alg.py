# 1 проверка наличия элемента в массиве
def search(arr, el): 
    for x in arr:
        if x == el:
            return True
    return False
  
# 2 поиск второго максимального элемента
def second_max(arr):
    if len(arr) < 2:
        return False
    max1 = max2 = arr[0]
    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2 and x != max1:
            max2 = x
    return max2

# 3 бинарный поиск
def bin_search(arr, el):
    sort_arr = sorted(arr)
    l, r = 0, len(sort_arr) - 1
    while l <= r:
        mid = (r + l) // 2
        if el > sort_arr[mid]:
            l = mid + 1
        elif el < sort_arr[mid]:
            r = mid - 1
        else:
            return True
    return False

# 4 построение таблицы умножения
def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

# 5 сортировка выбором
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    return arr

# функция измерения времени
import time
def measure_time(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start

# функция измерения времени и памяти
import tracemalloc
def measure_time_and_space(func, *args):
    tracemalloc.start()
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end - start, peak / 1024 
   
# функция генерации данных
import random
def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

sizes = [10, 100, 1000, 10000]
print("1. Проверка наличия элемента в массиве")
for size in sizes:
    test_arr = generate_array(size)
    execution_time = measure_time(search, test_arr, -1)
    print(f"Размер {size}: {execution_time:.8f} сек")

print("2. Поиск второго максимального элемента")
for size in sizes:
    test_arr = generate_array(size)
    execution_time = measure_time(second_max, test_arr)
    print(f"Размер {size}: {execution_time:.8f} сек")

print("3. Бинарный поиск")
for size in sizes:
    test_arr = generate_array(size)
    test_arr.sort()  
    execution_time = measure_time(bin_search, test_arr, test_arr[0])
    print(f"Размер {size}: {execution_time:.8f} сек")

sizes_table = [10, 50, 100]
print("4. Построение таблицы умножения")
for size in sizes_table:
    execution_time = measure_time(multiplication_table, size)
    print(f"Размер {size}: {execution_time:.8f} сек")

print("5. Сортировка выбором")
for size in sizes:
    test_arr = generate_array(size)
    execution_time, memory_kb = measure_time_and_space(selection_sort, test_arr)
    print(f"Размер {size}: {execution_time:.8f} сек, память: {memory_kb:.2f} КБ")
