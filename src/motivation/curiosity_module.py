import random

class CuriosityModule:
    def __init__(self):
        self.curiosity_level = 0.5  # средний интерес

    def assess_novelty(self, memory):
        """
        Анализирует память и выдаёт уровень любопытства.
        """
        delta = random.uniform(-0.1, 0.1)
        self.curiosity_level = max(0.0, min(1.0, self.curiosity_level + delta))
        print(f"[CuriosityModule] Текущий уровень любопытства: {self.curiosity_level:.2f}")
        return self.curiosity_level
