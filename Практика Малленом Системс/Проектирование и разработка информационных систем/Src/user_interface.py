# user_interface.py
import json
import os
from datetime import datetime
from image_processor import get_info, rename_file

class SimpleUI:
    def __init__(self):
        self.history = []
        self.load_history()
    
    def load_history(self):
        """Загрузить историю"""
        if os.path.exists("history.json"):
            with open("history.json", "r") as f:
                self.history = json.load(f)
    
    def save_history(self):
        """Сохранить историю"""
        with open("history.json", "w") as f:
            json.dump(self.history, f)
    
    def add_to_history(self, action, file_path):
        """Добавить в историю"""
        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "action": action,
            "file": os.path.basename(file_path)
        }
        self.history.append(record)
        self.save_history()
    
    def show_info(self):
        """Показать информацию о файле"""
        path = input("Путь к файлу: ")
        result = get_info(path)
        print(result)
        if "Ошибка" not in result:
            self.add_to_history("info", path)
    
    def rename_image(self):
        """Переименовать файл"""
        path = input("Путь к файлу: ")
        new_name = input("Новое имя: ")
        result = rename_file(path, new_name)
        print(result)
        if "Переименован" in result:
            self.add_to_history("rename", path)
    
    def show_history(self):
        """Показать историю"""
        if not self.history:
            print("История пуста")
            return
            
        for i, item in enumerate(self.history, 1):
            print(f"{i}. {item['date']} - {item['action']} - {item['file']}")
    
    def run(self):
        """Запустить программу"""
        while True:
            print("\n=== ПРОГРАММА ===")
            print("1 - Информация о файле")
            print("2 - Переименовать файл")
            print("3 - История")
            print("4 - Выход")
            
            choice = input("Выберите: ")
            
            if choice == "1":
                self.show_info()
            elif choice == "2":
                self.rename_image()
            elif choice == "3":
                self.show_history()
            elif choice == "4":
                break

# Запуск
if __name__ == "__main__":
    ui = SimpleUI()
    ui.run()