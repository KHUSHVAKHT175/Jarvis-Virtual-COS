import os
import json

# ----------------------------
# Импорты минимальных модулей
# ----------------------------
from modules.dialog.dialog import Dialog as DialogModule
from modules.scheduler.scheduler import SchedulerModule
from modules.logic.logic import LogicModule

# ----------------------------
# Настройки и реестры
# ----------------------------
module_registry = {
    "Dialog": "modules.dialog.dialog",
    "Scheduler": "modules.scheduler.scheduler",
    "Logic": "modules.logic.logic"
}

age_requirements = {
    "Dialog": 0,
    "Scheduler": 0,
    "Logic": 0
}

MEMORY_FILE = "src/core/memory_state.json"

# ----------------------------
# Memory
# ----------------------------
class HybridMemory:
    def __init__(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                try:
                    saved = json.load(f)
                except Exception:
                    saved = {}
            self.cache = saved.get("cache", {})
            self.archive = saved.get("archive", {})
            self.weights = saved.get("weights", {})
        else:
            self.cache = {}
            self.archive = {}
            self.weights = {}

    def store(self, task, result):
        self.cache[task["name"]] = result
        self.weights[task["name"]] = self.weights.get(task["name"], 1.0) + 0.1
        if len(self.cache) > 10:
            key, val = self.cache.popitem()
            self.archive[key] = val
        self.save()

    def get(self, key):
        return self.cache.get(key) or self.archive.get(key)

    def save(self):
        state = {"cache": self.cache, "archive": self.archive, "weights": self.weights}
        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)

    def clear_all(self):
        self.cache = {}
        self.archive = {}
        self.weights = {}
        self.save()

# ----------------------------
# Main
# ----------------------------
def main():
    print("=" * 32)
    print(" JARVIS‑COS Minimal: Терминальный запуск")
    print("=" * 32)
    try:
        user_age = int(input("Введите возраст пользователя: "))
    except Exception:
        user_age = 0

    # Подключаем минимальные модули
    modules = {
        "Dialog": DialogModule,
        "Scheduler": SchedulerModule,
        "Logic": LogicModule
    }

    memory = HybridMemory()

    print(f"\n[Jarvis‑COS] Модули: {list(modules.keys())}")
    print("Команды: 'chat', 'schedule', 'think', 'status', 'exit'\n")

    while True:
        cmd = input("Jarvis‑COS> ").strip()
        if cmd == "chat":
            if modules.get("Dialog"):
                modules["Dialog"].chat(memory)
            else:
                print("[Jarvis‑COS] Модуль Dialog не доступен.")
        elif cmd == "schedule":
            if modules.get("Scheduler"):
                modules["Scheduler"]().schedule()
            else:
                print("[Jarvis‑COS] Модуль Scheduler не доступен.")
        elif cmd == "think":
            if modules.get("Logic"):
                modules["Logic"]().think()
            else:
                print("[Jarvis‑COS] Модуль Logic не доступен.")
        elif cmd == "status":
            print(f"[Memory] Cache: {list(memory.cache.keys())}")
            print(f"[Memory] Archive: {list(memory.archive.keys())}")
        elif cmd == "magic":
            from modules.magic_field import MagicField
            MagicField().guess_number()

        elif cmd in ("exit", "shutdown", "stop"):
            print("[Jarvis‑COS Minimal] Завершение работы. Goodbye!")
            break
        else:
            print("[Jarvis‑COS Minimal] Только 'chat', 'schedule', 'think', 'status' или 'exit'.")

if __name__ == "__main__":
    main()
