# src/orchestrator.py (или main.py)

from modules.module_list import module_registry  # убрали age_requirements
from modules.reward_system import RewardSystem
from modules.curiosity_module import CuriosityModule
from modules.goal_setter import GoalSetter
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
        self.memory = HybridMemory()
        self.modules = self.load_allowed_modules()

        # --- Мотивационные модули ---
        from motivation.reward_system import RewardSystem
        from motivation.curiosity import CuriosityModule
        from motivation.goal_setter import GoalSetter

        self.reward_system = RewardSystem()
        self.curiosity_module = CuriosityModule()
        self.goal_setter = GoalSetter()

        print("[Orchestrator] Мотивационные модули инициализированы.")

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
        
        # --- Мотивационный цикл любопытства ---
        print("[Motivation] Оценка новизны через CuriosityModule...")
        curiosity_level = self.curiosity_module.assess_novelty(self.memory)
        print(f"[Motivation] Curiosity Level: {curiosity_level}")

        # --- Мотивационный цикл вознаграждения и адаптации ---
        print("[Motivation] Оценка результата через RewardSystem...")
        reward = self.reward_system.evaluate(success=True)  # success=True/False можно заменить на реальное условие
        print(f"[Motivation] Reward: {reward}")

        # --- Постановка новых целей ---
        print("[Motivation] Генерация новых целей через GoalSetter...")
        new_goals = self.goal_setter.generate_goals(curiosity_level, reward)
        print(f"[Motivation] New Goals: {new_goals}")

        # --- Сохранение мотивационных данных в память ---
        motivation_data = {
            "reward": reward,
            "curiosity": curiosity_level,
            "new_goals": new_goals,  
            "timestamp": time.time()
        }
        self.memory["motivation_log"] = self.memory.get("motivation_log", [])
        self.memory["motivation_log"].append(motivation_data)
        print("[Memory] Мотивационные данные сохранены в память.")

        # --- Коррекция весов ---
        
        if "AutoWeights" in self.modules:
            print("[Motivation] Коррекция весов по награде...")
            self.modules["AutoWeights"].update_weights(
                self.memory,
                reward=reward,
                curiosity=curiosity_level
            )
            # --- Логирование мотивационных параметров ---
            log_line = (
                f"[LOG] Reward={reward:.2f} | Curiosity={curiosity_level:.2f} | "
                f"Goals={len(new_goals) if new_goals else 0} | "
                f"Memory entries={len(self.memory.get('motivation_log', []))}"
            )
            print(log_line)

            # сохраняем лог в память
            self.memory["log"] = self.memory.get("log", [])
            self.memory["log"].append({
                "timestamp": time.time(),
                "reward": reward,
                "curiosity": curiosity_level,
                "goals": new_goals,
            })
