# Лабораторная работа №1
**Выполнила: Чернова Анастасия, ИДБ-25-07**

### 1. Проверка наличия элемента в массиве
Алгоритмическая сложность: O(n)
```python
def search(arr, el): 
    for x in arr:
        if x == el:
            return True
    return False
```
| n | Время (сек) |
|---|---|
| 10 | 0.00000248 |
| 100 | 0.00001421 |
| 1000 | 0.00001243 |
| 10000 | 0.00011919 |

### 2. Поиск второго максимального элемента
Алгоритмическая сложность: O(n)
```python
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
```
| n | Время (сек) |
|---|---|
| 10 | 0.00000398 |
| 100 | 0.00000472 |
| 1000 | 0.00002248 |
| 10000 | 0.00029223 |

### 3. Бинарный поиск
Алгоритмическая сложность: O(log n)
```python
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
```
| n | Время (сек) |
|---|---|
| 10 | 0.00000795 |
| 100 | 0.00000551 |
| 1000 | 0.00001665 |
| 10000 | 0.00015392 |

### 4. Построение таблицы умножения
Алгоритмическая сложность: O(n²)
```python
def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table
```
| n | Время (сек) |
|---|---|
| 10 | 0.00002055 |
| 50 | 0.00019704 |
| 100 | 0.00047649 |

### 5. Сортировка выбором
Алгоритмическая сложность: O(n²)

Пространственная сложность: O(n)
```python
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
```
| n | Время (сек) | Память (КБ) |
|---|---|---|
| 10 | 0.00003406 | 0.20 |
| 100 | 0.00021810 | 0.91 |
| 1000 | 0.26424000 | 8.09 |
| 10000 | 27.30140426 | 78.40 |
