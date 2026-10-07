# 7.	Статистика списка. Введи числа через пробел (input().split()). 
# Выведи: количество, сумму, среднее, минимум, максимум, отсортированный список и список без повторов 
# (подсказка: множеств ты ещё не знаешь, так что используй цикл с проверкой in).

text = input('Введи числа через пробел: ')
part = text.split()
numbers = [int(x) for x in part]
print(f"количество: {len(numbers)}")
print(f"сумма:{sum(numbers)}")
print(f"среднее: {sum(numbers)/len(numbers)}") 
print(f'минимум: {min(numbers)}')
print(f'максимум: {max(numbers)}')
print(f'отсортированный список: {sorted(numbers)}')
print(f'список без повторов через множества: {list(set(numbers))}')
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print(f'список без повторов НЕ через множества: {unique}')
