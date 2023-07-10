"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')
"""

import os


def parse_file_path(file):
    file_path, file_name = os.path.split(file)
    file_name, file_ext = os.path.splitext(file_name)
    return file_path, file_name, file_ext


path, name, extension = parse_file_path('/99890Desktop/курсы по Python/'
                                        'Урок-Погружение в Python(seminar)/lesson5/home_work/'
                                        'sss.md')
print(f' "{path}", "{name}", "{extension}"')
