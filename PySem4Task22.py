# Задача 22 (ДЗ):
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#  элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

# Вводим исходные данные
n = int(input("Введите кол-во элементов 1-го множества: "))
m = int(input("Введите кол-во элементов 2-го множества: "))

# генерируем первый список 
arrN = []
for i in range(n):
    arrN.append(int(randint(0,10)))

# генерируем второй список 
arrM = []
for i in range(m):
    arrM.append(int(randint(0,10)))

# Выводим в консоль сгенерированные списки
print(arrN)
print(arrM)

# Находим пересечение списков  Для этого преобразуем каждый список во множество set 
# и выполняем операцию пересечения & 
res = list(set(arrN) & set(arrM))

# Выводим результат в консоль
print(res)