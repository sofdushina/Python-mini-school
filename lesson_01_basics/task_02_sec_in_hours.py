#2.	Секунды в часы. 
# Введено количество секунд. Выведи в формате ЧЧ:ММ:СС, например 3725 → 01:02:05. 
# Подсказка: divmod и f"{x:02d}".
seconds = int(input("Введи количество секунд: "))
hours = seconds//3600
rest = seconds % 3600
minutes = rest//60
sec = rest%60
print(f'{hours:02d}:{minutes:02d}:{sec:02d}')

#Вариант с divmod
hours, rest = divmod(seconds,3600)
minutes, sec = divmod(rest,60)
print(f'{hours:02d}:{minutes:02d}:{sec:02d}')
