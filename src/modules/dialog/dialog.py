# src/modules/dialog/dialog.py
class Dialog:
    @staticmethod
    def chat(memory):
        print("[Dialog] Модуль запущен.")
        user_input = input("Введите сообщение: ")
        print(f"[Dialog] Вы сказали: {user_input}")
        # можно сохранять в память
        memory.store({"name": "last_chat"}, user_input)
