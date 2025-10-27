from src.core.layer_manager import LayerManager
from src.modules.example_module import ProcessLayer

if __name__ == "__main__":
    lm = LayerManager()
    inner = ProcessLayer("InnerLayer")
    outer = ProcessLayer("OuterLayer", inner_layer=inner)
    lm.add_layer(outer)

    print("Введите число для обработки слоями-матрёшками:")
    try:
        val = int(input("> "))
    except Exception:
        val = 0

    result = lm.run_all(val)
    print(f"Результат работы матрёшечных слоёв: {result}")
    print("\nСнимок состояния:")
    print(lm.snapshot_all())
