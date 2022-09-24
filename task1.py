# Задача: предложить улучшения кода для уже решённых задач (3-5 задач):

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]



# def nonrepeat(lst):
#     new_lst = []
    
#     for i in lst:
#         if lst.count(i) == 1:
#             new_lst.append(i)
#     return new_lst


lst = [1, 1, 2, 3, 4, 5, 5]
# print(nonrepeat(lst))

# или так
print([i for i in lst if lst.count(i) == 1])