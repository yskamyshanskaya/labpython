#лаб 2 вариант 5
#Написать функцию, которая принимает целочисленный
#список, состоящий из n элементов, и с помощью генераторного
#выражения создает и возвращает список, содержащий только
#положительный элементы входящего списка

my_list = ["1.1", "2.2", "3.3"]

def calculate_sum(arr):
    total = 0

    for num in arr:
        total += float(num)

    return total

result = calculate_sum(my_list)
print(result)