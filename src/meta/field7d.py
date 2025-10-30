class Field7D_Intent:
    def __init__(self):
        self.current_vector = "stable"
        self.resonance = 0.0

    def sense(self, system_state):
        # Анализ потока процессов, нагрузки, ошибок
        if system_state.get('load', 0) > 0.7:
            self.current_vector = "relax"
            self.resonance = 1.0
        elif system_state.get('errors', 0) > 2:
            self.current_vector = "restructure"
            self.resonance = 1.5
        else:
            self.current_vector = "flow"
            self.resonance = 0.5

    def influence(self, I1, I2):
        # Коррекция стратегий работы через намерение
        if self.current_vector == "relax" and hasattr(I1, "goal_mode"):
            I1.goal_mode = "optimize"
        elif self.current_vector == "restructure" and hasattr(I2, "repair_mode"):
            I2.repair_mode = True
        if hasattr(I1, 'log'):
            I1.log(f"[7D] Intent influence: {self.current_vector}")
        return self.current_vector
