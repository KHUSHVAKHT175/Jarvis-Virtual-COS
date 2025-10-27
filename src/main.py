from src.core.layer_manager import LayerManager
from src.modules.example_module import ProcessLayer

if __name__ == "__main__":
    lm = LayerManager()
    outer = ProcessLayer("OuterLayer")
    inner = ProcessLayer("InnerLayer")
    lm.add_layer(outer)
    lm.add_layer(inner)

    print("Тест: процессороёмкая задача — сумма квадратов N чисел.")
    result = lm.run_all(None)  # None — вход не нужен для теста

    print(f"\nФинальный результат через VM: {result}")
    print("\nСнимок состояния:")
    print(lm.snapshot_all())
