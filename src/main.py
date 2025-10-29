import importlib
import os
from decimal import Decimal

# --- Концепция многослойной виртуализации ("матрёшка") Virtual-COS ---
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

# --- Интеграция приложений через AppManager ---
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

# --- Адаптация, прозрачность, обратная связь (главная философия) ---
N = 50
history = []
max_load = 0.8

for i in range(N):
    print(f"\n--- Адаптивный цикл самообучения #{i+1} ---")
    # Динамическая нагрузка для реалистичной картины
    load = Decimal(str(round(0.6 + i * 0.006 + (i % 7) * 0.005, 3)))
    errors = int(max(0, (float(load) - max_load) * 10))
    am.run_app("monitor", {"load": float(load), "errors": errors, "active_layers": 2})

    # Обратная связь: если ошибок много — max_load понижается, если нет — повышается
    if errors > 2:
        max_load = round(max_load - 0.02, 3)
        am.run_app("event", f"Перегрузка, max_load уменьшен до {max_load}")
    elif errors == 0 and i > 0:
        max_load = round(min(max_load + 0.01, 0.95), 3)
        am.run_app("event", f"Успех, max_load увеличен до {max_load}")

    am.run_app("settings", "max_load", max_load)

    # Логирование истории для прозрачности анализа
    session = {"step": i+1, "load": float(load), "max_load": max_load, "errors": errors}
    history.append(session)
    am.run_app("logview", f"Сессия #{i+1}: нагрузка={float(load)}, max_load={max_load}, ошибок={errors}")
    am.run_app("demo_selflearn", f"Адаптивный обучающий цикл №{i+1}")

    # Автоматическая остановка при достижении устойчивого успеха (главный критерий сходимости)
    if len(history) >= 5 and all(h["errors"] == 0 for h in history[-5:]):
        print(f"\n[STOP] Самообучение завершено на {i+1} цикле — стабильность и качество достигнуты!")
        break

print("\n--- Самообучение завершено ---")
am.run_app("logview")
am.run_app("settings")
am.run_app("demo_selflearn")
