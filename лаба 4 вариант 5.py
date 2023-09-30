#лаб 4 вариант 5
#Написать функцию, которая принимает объект datetime
#и возвращает номер дня в году.
from datetime import date
first_date = date.today()
second_date = date(2022, 12, 31)
delta = first_date - second_date
print(delta)