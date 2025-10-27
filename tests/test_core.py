import pytest
from src.core.layer import Layer
from src.core.virtual_processor import VirtualProcessor
from src.core.layer_manager import LayerManager
from src.modules.example_module import ProcessLayer

def test_layer_run():
    l = Layer("test")
    assert l.run(5) == 5
    snap = l.snapshot()
    l.restore(snap)
    assert l.state == 'initialized'

def test_virtual_processor_basic():
    vp = VirtualProcessor("vp_test")
    instructions = [
        {"op": "SET", "args": [0, 10]},
        {"op": "SET", "args": [1, 20]},
        {"op": "ADD", "args": [2, 0, 1]}, # r2 = r0 + r1
    ]
    vp.execute(instructions)
    assert vp.registers[2] == 30

def test_process_layer():
    pl = ProcessLayer("PL1")
    result = pl.run(8)
    assert result == 50  # 42 + 8

def test_layer_manager_matrjoshka():
    lm = LayerManager()
    inner = ProcessLayer("InnerLayer")
    outer = ProcessLayer("OuterLayer", inner_layer=inner)
    lm.add_layer(outer)
    out = lm.run_all(4)
    assert out == 46  # 42 + 4 обработал внутренний слой
