#лаб 1 вариант 5
#Написать функцию, которая принимает целочисленный
#список и возвращает True, если длина списка больше нуля и
#первый и последний элемент списка равны.

def test(arr):
    if len(arr) == 0:
        return False
    if arr[0] == arr[-1]:
        return True
    else:
        return False

# Пример использования функции
result = test([3, 5])
print(result)