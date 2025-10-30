class Field15D_Core:
    def __init__(self, fields):
        self.fields = fields
        self.global_state = "balanced"

    def evaluate(self):
        # Суммируем резонансы для оценки стабильности
        resonance = sum(getattr(f, 'resonance', 0) for f in self.fields)
        if resonance > 2.5:
            self.global_state = "unstable"
        else:
            self.global_state = "balanced"
        return self.global_state

    def broadcast(self):
        print(f"[15D] Core state: {self.global_state}")
