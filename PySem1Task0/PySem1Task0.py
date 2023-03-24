# Задача №0
# Найти наибольшее число из двух

#  Функция читает данные от пользователя, и преобразует их в int
def read_data(str):
    return int(input(str))

# Функция находит наибольшее число из двух

def max_num(num1,num2):
    maxNum = 0
    if num1 > num2:
        maxNum = num1
        print(f"Максимальное число равно: {maxNum}")
    elif num1 == num2:
        print(f"Число А {num1} = числу Б {num2}")
    else:
        maxNum = num2
        print(f"Максимальное число равно: {maxNum}")
    

# Основной код программы
# Вводим данные с консоли
firstNum = read_data("Введите число А: ")
secondNum = read_data("Введите число Б: ")

# Вычисляем макс введенное число
max_num(firstNum,secondNum)

