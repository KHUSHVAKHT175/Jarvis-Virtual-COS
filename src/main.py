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
