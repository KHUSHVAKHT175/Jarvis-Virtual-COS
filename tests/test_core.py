from src.modules.example_module import ProcessLayer
import time

def test_vm_vs_native():
    N = 1000  # маленький N - чтобы не затормозить тест

    arr = list(range(N))
    t0 = time.time()
    r_py = sum([x*x for x in arr])
    t1 = time.time()
    py_time = t1 - t0

    layer = ProcessLayer("LayerTest")
    # Переопредели N внутри process() на N = 1000 для теста
    result = layer.process(None)
    assert result == r_py
    print(f"Python: {py_time:.4f}s, VM 'виртуальных': {layer.vproc.virtual_time}")

if __name__ == "__main__":
    test_vm_vs_native()
    print("Тест пройден!")
