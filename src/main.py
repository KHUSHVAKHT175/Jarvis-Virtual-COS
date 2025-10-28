from src.core.layer_manager import LayerManager
from src.modules.example_module import ProcessLayer

if __name__ == "__main__":
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
