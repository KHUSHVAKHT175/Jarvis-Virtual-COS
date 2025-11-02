# src/orchestrator.py (или main.py)

from modules.module_list import module_registry  # убрали age_requirements

class HybridMemory:
    def __init__(self):
        self.cache = {}
        self.archive = {}
        self.weights = {}

    def store(self, task, result):
        self.cache[task["name"]] = result
        self.weights[task["name"]] = self.weights.get(task["name"], 1.0) + 0.1
        if len(self.cache) > 10:
            key, val = self.cache.popitem()
            self.archive[key] = val

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        if key in self.archive:
            return self.archive[key]
        return None

class Orchestrator:
    def __init__(self):
        self.modules = self.load_allowed_modules()
        self.memory = HybridMemory()

    def load_allowed_modules(self):
        allowed = {}
        for name, path in module_registry.items():
            allowed[name] = __import__(path, fromlist=[""])
        return allowed

    def run(self):
        print(f"Доступные модули: {list(self.modules.keys())}")

        if "AutoWeights" in self.modules:
            print("[Orchestrator] Автоподстройка весов памяти...")
            self.modules["AutoWeights"].night_optimize_weights(self.memory)
            print(f"Веса памяти: {self.memory.weights}")

        if "NightOptimizer" in self.modules:
            print("[Orchestrator] Запуск NightOptimizer")
            self.modules["NightOptimizer"].run_night_cycle(self.memory, active=True)