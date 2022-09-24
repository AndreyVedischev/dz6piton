# Задача: предложить улучшения кода для уже решённых задач (3-5 задач):

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


a_list = [1.1, 1.2, 3.1, 5, 10.01]

# def difference_elements(lst):
#     lst = []
#     for i in a_list:
#         if i %1 != 0:
#             lst.append(round(i%1,2))
#     print(max(lst)-min(lst))


# difference_elements(a_list)

# Улучшение

lst = list(map(float, a_list))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))