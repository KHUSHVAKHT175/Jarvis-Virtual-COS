import importlib
import os
from decimal import Decimal

# --- LayerManager блок: архитектура виртуализации, многослойности и когнитивного выбора ---
from src.core.layer_manager import LayerManager
from src.modules.example_module import ProcessLayer

lm = LayerManager()
outer = ProcessLayer("OuterLayer")
inner = ProcessLayer("InnerLayer")
lm.add_layer(outer)
lm.add_layer(inner)

print("Virtual-COS: демонстрация многослойности, виртуализации и когнитивного выбора ОС.")
result = lm.run_all(None)
print("\nИтог вычислений:", result)
print("\nСостояние слоёв и логи:")
for snapshot in lm.snapshot_all():
    print(snapshot)

# --- AppManager блок ---
from src.core.app_manager import AppManager

am = AppManager()
am.discover_apps()

print("\nVirtual-COS: список штатных приложений")
print(am.list_apps())

print("Запуск калькулятора:")
am.run_app("calc", 2, 3)

print("Запуск редактора:")
am.run_app("edit", "example.txt", "Это тестовая запись в файл для Virtual-COS.")
am.run_app("edit", "example.txt")

print("Статус проводника:")
print(am.status("fexplorer"))

# --- Финальное самообучение с контролем стабильности и точности float ---
N = 50
errors_prev = None
load_prev = None
stable_cycles = 0
STABILITY_REQUIRED = 5  # Сколько циклов подряд стабильной статистики требуется

for i in range(N):
    print(f"\n--- Цикл самообучения #{i+1} ---")
    load = Decimal(str(round(0.6 + i * 0.006, 3)))
    errors = i % 4
    am.run_app("monitor", {"load": float(load), "errors": errors, "active_layers": 2})
    max_load = float(round(0.8 - i * 0.01, 3))
    am.run_app("settings", "max_load", max_load)
    am.run_app("logview", f"Сессия #{i+1}: нагрузка={float(load)}, ошибок={errors}")
    am.run_app("demo_selflearn", f"Обучающий цикл №{i+1}")

    # --- контроль стабильности ---
    if errors_prev == errors and load_prev == load:
        stable_cycles += 1
        if stable_cycles >= STABILITY_REQUIRED:
            print(f"\n[STOP] Самообучение завершено на {i+1} цикле — стабильность метрик достигнута!")
            break
    else:
        stable_cycles = 0

    errors_prev = errors
    load_prev = load

print("\n--- Самообучение завершено ---")
am.run_app("logview")
am.run_app("settings")
am.run_app("demo_selflearn")
