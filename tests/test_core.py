from src.modules.example_module import ProcessLayer
import time

def test_vm_vs_native():
    N = 1000  # �����쪨� N - �⮡� �� ���ମ���� ���

    arr = list(range(N))
    t0 = time.time()
    r_py = sum([x*x for x in arr])
    t1 = time.time()
    py_time = t1 - t0

    layer = ProcessLayer("LayerTest")
    # ��८�।��� N ����� process() �� N = 1000 ��� ���
    result = layer.process(None)
    assert result == r_py
    print(f"Python: {py_time:.4f}s, VM '����㠫���': {layer.vproc.virtual_time}")

if __name__ == "__main__":
    test_vm_vs_native()
    print("���� �ன���!")
