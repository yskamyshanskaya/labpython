#лаб 2 вариант 5
#Написать функцию, которая принимает список, состоящий из строк, которые являются целочисленными значениями
#или значениями с плавающей точкой, и возвращает их сумму.

my_list = ["1.1", "2.2", "3.3"]

def calculate_sum(arr):
    total = 0

    for num in arr:
        total += float(num)

    return total

result = calculate_sum(my_list)
print(result)