#лаб 3 вариант 5
def positive_numbers_generator(input_list):
    return [num for num in input_list if num > 0]
my_list = [1, -2, 3, -4, 5]
result = positive_numbers_generator(my_list)
print(result)
# Вывод: [1, 3, 5]
#Написать функцию, которая принимает целочисленный
#список, состоящий из n элементов, и с помощью генераторного
#выражения создает и возвращает список, содержащий только
#положительный элементы входящего списка.
def positive_numbers_generator(input_list):
    return [num for num in input_list if num > 0]
my_list = [1, -2, 3, -4, 5]
result = positive_numbers_generator(my_list)
print(result)
# Вывод: [1, 3, 5]