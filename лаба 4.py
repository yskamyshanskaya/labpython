#лаб 4 вариант 5
#Написать программу, которая принимает путь к файлу
#и возвращает True или False в зависимости от того, доступен ли
#файл для чтения и записи или нет.

import os

def check_file_accessibility(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
            return True
    return False

# Пример использования программы
file_path = "/путь/к/вашему/файлу"  # Замените на путь к вашему файлу
is_accessible = check_file_accessibility(file_path)

if is_accessible:
    print("Файл доступен для чтения и записи.")
else:
    print("Файл не доступен для чтения и/или записи.")