import os
import shutil
from utils import is_within_work_dir

class FileManager:
    '''методы для работы c файлами и папками (создание, удаление, перемещение и т.д.)'''

    def __init__(self, work_dir):
        self.work_dir = work_dir
        self.current_dir = work_dir

    def create_dir(self, name):
        '''Создает директорию'''
        path = os.path.join(self.current_dir, name)
        if not is_within_work_dir(path):
            print("Ошибка: выход за пределы рабочей директории")
            return
        if os.path.exists(path):
            print("Ошибка: директория уже существует")
        else:
            os.makedirs(path)
            print(f"Директория '{name}' создана")

    def delete_dir(self, name):
        '''Удаляет директорию, проверяя, что она пуста'''
        path = os.path.join(self.current_dir, name)
        if not is_within_work_dir(path):
            print("Ошибка: выход за пределы рабочей директории")
            return
        if not os.path.exists(path):
            print("Ошибка: директория не существует")
        elif not os.path.isdir(path):
            print("Ошибка: это не директория")
        elif os.listdir(path):
            print("Ошибка: директория не пуста")
        else:
            os.rmdir(path)
            print(f"Директория '{name}' удалена")

    def navigate(self, path):
        '''Изменяет текущую директорию'''
        new_path = os.path.join(self.current_dir, path)
        if not is_within_work_dir(new_path):
            print("Ошибка: выход за пределы рабочей директории")
            return
        if not os.path.exists(new_path):
            print("Ошибка: путь не существует")
        elif not os.path.isdir(new_path):
            print("Ошибка: это не директория")
        else:
            self.current_dir = new_path
            print(f"Текущая директория: {self.current_dir}")

    def create_file(self, name):
        '''Создает пустой файл'''
        path = os.path.join(self.current_dir, name)
        if not is_within_work_dir(path):
            print("Ошибка: выход за пределы рабочей директории")
            return
        if os.path.exists(path):
            print("Ошибка: файл уже существует")
        else:
            open(path, 'x').close()
            print(f"Файл '{name}' создан")

    def read_file(self, name):
        '''Выводит содержимое файла'''
        path = os.path.join(self.current_dir, name)
        if not is_within_work_dir(path):
            print("Ошибка: выход за пределы рабочей директории")
            return
        if not os.path.exists(path):
            print("Ошибка: файл не существует")
        elif not os.path.isfile(path):
            print("Ошибка: это не файл")
        else:
            with open(path, 'r') as f:
                content = f.read()
                print(content)

    def write_file(self, name, content):
        '''Записывает контент в файл'''
        path = os.path.join(self.current_dir, name)
        if not is_within_work_dir(path):
            print("Ошибка: выход за пределы рабочей директории")
            return
        try:
            with open(path, 'w') as f:
                for line in content:
                    f.write(line + ' ')
                print(f"Содержание записано в файл '{name}'")
        except OSError as e:
            print(f"Ошибка записи в файл: {e}")

    def delete_file(self, name):
        '''Удаляет файл'''
        path = os.path.join(self.current_dir, name)
        if not is_within_work_dir(path):
            print("Ошибка: выход за пределы рабочей директории")
            return
        if not os.path.exists(path):
            print("Ошибка: файл не существует")
        elif not os.path.isfile(path):
            print("Ошибка: это не файл")
        else:
            os.remove(path)
            print(f"Файл '{name}' удален")
    
    def copy_file(self, source, destination):
        '''Копирует файл'''
        source_path = os.path.join(self.current_dir, source)
        dest_path = os.path.join(self.current_dir, destination)
        if not is_within_work_dir(source_path) or not is_within_work_dir(dest_path):
            print("Ошибка: выход за пределы рабочей директории")
            return
        if not os.path.exists(source_path):
            print("Ошибка: исходный файл не существует")
        elif os.path.exists(dest_path):
            print("Ошибка: файл назначения уже существует")
        else:
            try:
                shutil.copy2(source_path, dest_path)
                print(f"Файл '{source}' скопирован в '{destination}'")
            except OSError as e:
                print(f"Ошибка копирования файла: {e}")
    
    def move_file(self, source, destination):
        '''Перемещает файл'''
        source_path = os.path.join(self.current_dir, source)
        dest_path = os.path.join(self.current_dir, destination)
        if not is_within_work_dir(source_path) or not is_within_work_dir(dest_path):
            print("Ошибка: выход за пределы рабочей директории")
            return
        if not os.path.exists(source_path):
            print("Ошибка: исходный файл не существует")
        else:
            try:
                shutil.move(source_path, dest_path)
                print(f"Файл '{source}' перемещен в '{destination}'")
            except OSError as e:
                print(f"Ошибка перемещения файла: {e}")

    def rename_file(self, old_name, new_name):
        '''Переименовывает файл'''
        old_path = os.path.join(self.current_dir, old_name)
        new_path = os.path.join(self.current_dir, new_name)
        if not is_within_work_dir(old_path) or not is_within_work_dir(new_path):
            print("Ошибка: выход за пределы рабочей директории")
            return
        if not os.path.exists(old_path):
            print("Ошибка: исходный файл не существует")
        elif os.path.exists(new_path):
            print("Ошибка: файл с новым именем уже существует")
        else:
            os.rename(old_path, new_path)
            print(f"Файл '{old_name}' переименован в '{new_name}'")
    
    