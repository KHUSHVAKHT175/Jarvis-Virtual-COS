import importlib
import os

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

# --- AppManager блок: внедрённый штатный набор приложений Virtual-COS ---
from src.core.app_manager import AppManager

am = AppManager()
am.discover_apps()

print("\nVirtual-COS: список штатных приложений")
print(am.list_apps())

print("Запуск калькулятора:")
am.run_app("calc", 2, 3)

print("Запуск редактора:")
am.run_app("edit", "example.txt")

print("Статус проводника:")
print(am.status("fexplorer"))
from src.core.app_manager import AppManager

am = AppManager()
am.discover_apps()

# 1. Основной мониторинг ресурсов и ошибок
am.run_app("monitor", {"load":0.7, "errors":1, "active_layers":2})

# 2. Логирование важных событий в работе слоёв и приложений
am.run_app("logview", "Layer Outer запущен без ошибок")
am.run_app("logview", "Изменение конфигурации max_load")

# 3. Автокорректировка параметров на основе мониторинга
am.run_app("settings", "max_load", 0.6)
am.run_app("settings")

# 4. Отработка событий рефлексов и обратной связи
am.run_app("event", "Перегрузка ядра")
am.run_app("event", "Переключение слоя на резервный")

# 5. Синхронизация — запуск в sandbox/test режиме
am.run_app("sync")

# 6. Обновление системы — запуск тестового изменения
am.run_app("update")

# 7. Демонстрация обучающих шагов (test-тasks)
am.run_app("demo_selflearn", "Собрать статистику ошибок за сутки")
am.run_app("demo_selflearn", "Изменить конфиг на max_load=0.5")
am.run_app("demo_selflearn")
for _ in range(5):
    # Эмуляция нагрузки и ошибок
    current_load = 0.8  # допустим, тренируем на большой нагрузке
    am.run_app("monitor", {"load": current_load, "errors": 2, "active_layers": 1})
    if current_load > 0.7:
        am.run_app("event", "Перегрузка")
        am.run_app("settings", "max_load", 0.6)  # система сама снижает порог
        am.run_app("logview", "max_load понижен до 0.6 в режиме обучения")
    am.run_app("demo_selflearn", f"Шаг обучения (нагрузка={current_load})")
# --- Финальное самообучение системы Virtual-COS ---

N = 50  # количество обучающих циклов

for i in range(N):
    print(f"\n--- Цикл самообучения #{i+1} ---")
    # Запуск мониторинга состояния
    am.run_app("monitor", {"load": 0.6 + i * 0.006, "errors": i % 4, "active_layers": 2})
    # Лог событий
    am.run_app("logview", f"Сессия #{i+1}: нагрузка={0.6 + i * 0.006}, ошибок={i % 4}")
    # Адаптация параметров
    am.run_app("settings", "max_load", 0.8 - i * 0.01)
    # Вызов событий (перегрузка, откат, тест)
    if i % 10 == 0:
        am.run_app("event", "Критическая нагрузка, запуск резервного слоя")
    # Синхронизация и обновление по мере обучения
    if i % 15 == 0:
        am.run_app("sync")
        am.run_app("update")
    # Демонстрация шага обучения
    am.run_app("demo_selflearn", f"Обучающий цикл №{i+1}")

print("\n--- Самообучение завершено ---")
am.run_app("logview")        # вывести финальный лог
am.run_app("settings")       # показать итоговый конфиг
am.run_app("demo_selflearn") # показать шаги обучения
