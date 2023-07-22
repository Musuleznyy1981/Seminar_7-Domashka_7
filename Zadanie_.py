# Мусулезный Максим 22.07.2023 Задание 1
# Напишите функцию группового переименования файлов. Она должна:
# Принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# Принимать параметр количество цифр в порядковом номере.
# Принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# Принимать параметр расширение конечного файла.
# Принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.

import os
from pathlib import Path


def group_rename(count_len: int, extension: str, new_extension: str, interval: list[int], new_name=''):
    count = 0
    for file in os.listdir():
        if file.endswith(extension):
            count += 1
            Path(file).rename(f"{file.split('.')[0][interval[0]:interval[1]]}{new_name}{count:0>{count_len}}.{new_extension}")


group_rename(4, 'pip', 'zip', [2, 4], "new")

