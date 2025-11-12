# image_processor.py
import os
from PIL import Image
import datetime

def get_info(path):
    """Получить информацию об изображении"""
    try:
        if not os.path.exists(path):
            return "Файл не найден"
        
        img = Image.open(path)
        width, height = img.size
        
        # Размер файла
        size = os.path.getsize(path)
        if size < 1024*1024:
            size_text = f"{size/1024:.1f} KB"
        else:
            size_text = f"{size/(1024*1024):.1f} MB"
        
        # Дата создания
        create_time = os.path.getctime(path)
        create_date = datetime.datetime.fromtimestamp(create_time)
        date_text = create_date.strftime("%Y-%m-%d %H:%M")
        
        info = f"""
Файл: {os.path.basename(path)}
Размер: {width} x {height}
Вес: {size_text}
Формат: {img.format}
Дата создания: {date_text}
"""
        img.close()
        return info
        
    except Exception as e:
        return f"Ошибка: {e}"

def rename_file(path, new_name):
    """Переименовать файл"""
    try:
        if not os.path.exists(path):
            return "Файл не найден"
        
        # Получаем расширение файла
        ext = os.path.splitext(path)[1]
        folder = os.path.dirname(path)
        
        # Новый путь
        new_path = os.path.join(folder, new_name + ext)
        
        # Переименовываем
        os.rename(path, new_path)
        return f"Переименован в: {new_name + ext}"
        
    except Exception as e:
        return f"Ошибка: {e}"

# Простое меню
if __name__ == "__main__":
    while True:
        print("\n1 - Информация о файле")
        print("2 - Переименовать файл") 
        print("3 - Выход")
        
        choice = input("Выберите: ")
        
        if choice == "1":
            path = input("Путь к файлу: ")
            print(get_info(path))
            
        elif choice == "2":
            path = input("Путь к файлу: ")
            new_name = input("Новое имя: ")
            print(rename_file(path, new_name))
            
        elif choice == "3":
            break