from src.core.layer import Layer
from src.core.virtual_processor import VirtualProcessor

class ProcessLayer(Layer):
    def __init__(self, name, inner_layer=None, params=None):
        super().__init__(name, inner_layer, params)
        self.vproc = VirtualProcessor(f"{name}_vproc")
    
    def process(self, data):
        instructions = [
            {"op": "SET", "args": [0, 42]},  # r0 = 42
            {"op": "SET", "args": [1, data if data is not None else 0]},   # r1 = data
            {"op": "ADD", "args": [2, 0, 1]},  # r2 = r0 + r1
            {"op": "PRINT", "args": [2]},   # вывести r2
        ]
        self.vproc.execute(instructions)
        return self.vproc.registers[2]
