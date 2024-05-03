import os 
from file_manager import FileManager
import config

def main():
    file_manager = FileManager(config.WORK_DIR) 

    while True:
        #Получает команду от пользователя
        command = input(f"{file_manager.current_dir}> ") 
        #Разделяет команду на аргументы
        args = command.split() 

        if not args: 
            continue
        
        #Проверяет первую часть команды и
        #вызывает соответствующий метод FileManager с аргументами
        if args[0] == 'exit':
            break

        elif args[0] == 'cd':
            if len(args) < 2:
                print("Ошибка: укажите путь") 
            else:
                file_manager.navigate(args[1])

        elif args[0] == 'mkdir':
            if len(args) < 2:
                print("Ошибка: укажите имя директории")
            else:
                file_manager.create_dir(args[1])

        elif args[0] == 'rm':
            if len(args) < 2:
                print("Ошибка: укажите имя файла")
            else:
                file_manager.delete_file(args[1])

        elif args[0] == 'rmdir':
            if len(args) < 2:
                print("Ошибка: укажите имя директории")
            else:
                file_manager.delete_dir(args[1])

        elif args[0] == 'cat':
            if len(args) < 2:
                print("Ошибка: укажите имя файла")
            else:
                file_manager.read_file(args[1])

        elif args[0] == 'touch':
            if len(args) < 2:
                print("Ошибка: укажите имя файла")
            else:
                file_manager.create_file(args[1])

        elif args[0] == 'cp':
            if len(args) < 3:
                print("Ошибка: укажите исходный и целевой файлы")
            else:
                file_manager.copy_file(args[1], args[2])

        elif args[0] == 'mv':
            if len(args) < 3:
                print("Ошибка: укажите исходный и целевой файлы")
            else:
                file_manager.move_file(args[1], args[2])

        elif args[0] == 'rename':
            if len(args) < 3:
                print("Ошибка: укажите старое и новое имя файла")
            else:
                file_manager.rename_file(args[1], args[2])

        elif args[0] == 'write':
            if len(args) < 3:
                print("Ошибка: укажите название файла и контент для записи через пробелы")
            else:
                file_manager.write_file(args[1], args[2:])

        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()