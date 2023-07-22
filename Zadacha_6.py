from Zadacha_5 import gen_files
from pathlib import Path
import os


def create_dir(name_dir: str):
    #name = Path(name_dir)   # new
    #path = name.cwd() / name_dir  # C:\Users\maksi\PycharmProjects\pythonDomashka__7_22.07.2023\Zadacha_5_new .py
    name = Path(Path.cwd() / name_dir) # C:\Users\maksi\PycharmProjects\pythonDomashka__7_22.07.2023\Zadacha_5_new .py
    if not name.exists():       #проверка на наличие директория
        name.mkdir()            #создает директорий с именем name_dir в текущем директории

    os.chdir(name)          #переходим в созданный каталог сделав его текущим


if __name__ == '__main__':
    my_dict = {'.txt': 1, '.doc': 1, '.bin': 1, '.pdf': 1}
    gen_files(my_dict)
    create_dir('new')