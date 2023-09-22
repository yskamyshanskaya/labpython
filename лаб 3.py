#лаб 3
#Написать функцию, которая принимает объект datetime
#и возвращает номер дня в году.

import datetime

def day_of_year(date):
    if not isinstance(date, datetime.datetime):
        raise ValueError("Input must be a datetime object")

    return date.timetuple().tm_yday

# Пример использования функции
date = datetime.datetime(2023, 9, 22)  # Замените эту дату на нужную
day_number = day_of_year(date)
print(f"Номер дня в году: {day_number}")