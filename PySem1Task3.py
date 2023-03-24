# Задача No3. Решение в группах
# В некоторой школе решили набрать три новых математических класса 
# и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.



#  Функция читает данные от пользователя, и преобразует их в int
def read_data(str):
    return int(input(str))
# Функция считает необходимое количество парт в классе
def desk_of_class(student_num):

    # считаем количество парт используя целочисленное деление
    res = (student_num + 1) // 2
    return res


# Основной код программы
# Вводим данные с консоли
student_of_first_class = read_data("Введите количество учеников в 1 классе: ")
student_of_second_class = read_data("Введите количество учеников во 2 классе: ")
student_of_third_class = read_data("Введите количество учеников в 3 классе: ")

# Считаем необходимое кол-во парт в каждом классе
desk_first_class = desk_of_class(student_of_first_class)
desk_second_class = desk_of_class(student_of_second_class)
desk_third_class = desk_of_class(student_of_third_class)

# Считаем общее кол-во парт и учеников
all_desk = desk_first_class + desk_second_class + desk_third_class
all_student = student_of_first_class + student_of_second_class + student_of_third_class

# Выводим результат в консоль
print(f"Что бы разместить всех {all_student} учеников необходимо {all_desk} парт")