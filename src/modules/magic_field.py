import random
import json
import os

MEMORY_FILE = "src/core/memory_state.json"

class MagicField:
    def __init__(self):
        self.attempts = 0
        self.success = 0
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("magic_field", {"intuition_bias": 0.5})
            except Exception:
                return {"intuition_bias": 0.5}
        return {"intuition_bias": 0.5}

    def save_memory(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {}
        data["magic_field"] = self.memory
        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def guess_number(self):
        print("[Jarvis-COS Magic] Запуск интуитивного поля угадывания.")
        print("Загадай число от 1 до 9. (не говори)")
        bias = self.memory.get("intuition_bias", 0.5)
        while True:
            n = random.randint(1, 9)
            print(f"[Logic] Пробую почувствовать... может быть {n}?")
            resp = input("Попал? (y/n): ").strip().lower()
            self.attempts += 1
            if resp == "y":
                print("[Jarvis-COS] Отлично! Я учту это в памяти поля.")
                self.success += 1
                self.memory["intuition_bias"] = min(1.0, bias + 0.05)
                self.save_memory()
                break
            elif resp == "n":
                print("[Logic] Ловлю другой поток... пробую снова.")
                bias = max(0.1, bias - 0.01)
            else:
                print("[System] Введите только 'y' или 'n'.")
