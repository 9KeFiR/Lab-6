import os
import config

def is_within_work_dir(path):
    '''Функция is_within_work_dir проверяет, 
    находится ли путь внутри рабочей директории, 
    прежде чем выполнять операции с файлами или папками. 
    Это обеспечивает безопасность и предотвращает случайное
    изменение файлов вне рабочей области.'''
    abs_path = os.path.abspath(path)
    abs_work_dir = os.path.abspath(config.WORK_DIR)
    return os.path.commonpath([abs_path, abs_work_dir]) == abs_work_dir