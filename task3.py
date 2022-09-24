# Задача: предложить улучшения кода для уже решённых задач (3-5 задач):

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['efg23', '79234gefg', 'sdgs', 'g53']

# def find(lst, finddigit):

# 	for i in range(len(lst)):
# 		if finddigit in lst[i]:
# 			print(lst[i])


lst = ['efg23', '79234gefg', 'sdgs', 'g53']
finddigit = '2'

# find(lst, finddigit)

new_lst = [i for i in range(len(lst)) if finddigit in lst[i]]
print(f'Присутствует в строке с индексом{new_lst}')