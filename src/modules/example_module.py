from src.core.layer import Layer
from src.core.virtual_processor import VirtualProcessor
import time

class ProcessLayer(Layer):
    def __init__(self, name, inner_layer=None, params=None):
        super().__init__(name, inner_layer, params)
        self.vproc = VirtualProcessor(f"{name}_vproc")

    def process(self, data):
        N = 100_000  # размер задачи (можно менять)
        # ========== Python native ==========
        arr = list(range(N))
        start_py = time.time()
        result_py = sum([x*x for x in arr])
        end_py = time.time()
        print(f"Python native: result = {result_py}, time = {end_py-start_py:.3f} сек")

        # ========== Jarvis VM ==========
        # Подать массив в память VM
        self.vproc.memory = {i: i for i in range(N)}
        self.vproc.virtual_time = 0  # сбрасываем виртуальное время

        instructions = []
        # r0 - индекс, r1 - сумма, r2 - текущий элемент, r3 - квадрат
        instructions.append({"op": "SET", "args": [0, 0]})  # r0 = 0
        instructions.append({"op": "SET", "args": [1, 0]})  # r1 = 0

        for i in range(N):
            # Каждый шаг - "физически" проходит один цикл, а "виртуально" может быть любым
            instructions += [
                {"op": "LOAD", "args": [2, i]},       # r2 = arr[i]
                {"op": "MUL", "args": [3, 2, 2]},    # r3 = r2 * r2
                {"op": "ADD", "args": [1, 1, 3]},    # r1 += r3
            ]

        instructions.append({"op": "PRINT", "args": [1]})

        # --- Изменяем законы "виртуального времени" ---
        # Добавь поле/логику в VirtualProcessor, если нужно асимметричное потребление:
        # Например, для MUL: self.virtual_time += 10, для ADD: += 1, для LOAD: += 2.

        start_vm = time.time()
        self.vproc.execute(instructions)
        end_vm = time.time()
        print(f"Jarvis VM: result = {self.vproc.registers[1]}, real time = {end_vm-start_vm:.3f} сек, virtual time = {self.vproc.virtual_time} тактов")

        return self.vproc.registers[1]
