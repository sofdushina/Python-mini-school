#6.	Динамическое программирование: лесенка. 
# Ты поднимаешься по лестнице из n ступенек и за раз можешь шагнуть на 1 или на 2 ступеньки.
# Сколько существует способов подняться наверх? Напиши функцию ways(n) 
# двумя способами: наивной рекурсией и с @cache. 
# Сравни время для n = 35.
# Проверка: ways(1) → 1, ways(2) → 2, ways(5) → 8.
# Подсказка: как можно оказаться на ступеньке n? Только шагнув с n-1 или с n-2.
# Подумай, какое это соотношение (оно тебе знакомо из этого урока) и какие базовые случаи.

def ways(n): #наивной рекурсией
    if n ==1:
        return 1
    if n == 2:
        return 2
    return ways(n-1)+ways(n-2)
print (ways(5))

from functools import cache

@cache
def ways_cache(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return ways_cache(n-1) + ways_cache(n-2)
print(ways_cache(5))

import time

start = time.perf_counter()
print(ways(35))
print(f"наивно: {time.perf_counter() - start:.2f} с")

start = time.perf_counter()
print(ways_cache(35))
print(f"с кэшем: {time.perf_counter() - start:.5f} с")