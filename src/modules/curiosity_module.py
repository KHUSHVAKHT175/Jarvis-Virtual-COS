# src/modules/curiosity_module.py
class CuriosityModule:
    def assess_novelty(self, memory):
        novelty = random.uniform(0.0, 1.0)
        print(f"[CuriosityModule] → Уровень новизны = {novelty:.2f}")
        return novelty
