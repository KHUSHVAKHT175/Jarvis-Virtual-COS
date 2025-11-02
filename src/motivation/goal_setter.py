# src/motivation/goal_setter.py

class GoalSetter:
    """Модуль постановки целей. Создает новые цели на основе любопытства и награды."""

    def __init__(self):
        self.last_goals = []

    def generate_goals(self, curiosity_level, reward):
        # Простая логика: чем выше любопытство и награда, тем больше целей рождается
        base_goals = ["анализ данных", "поиск новых связей", "оптимизация алгоритмов"]
        curiosity_factor = int(curiosity_level * 3)
        reward_factor = int(reward * 2)

        total_new_goals = max(1, curiosity_factor + reward_factor)
        new_goals = base_goals[:total_new_goals % len(base_goals)]
        if not new_goals:
            new_goals = ["повторить исследование"]

        self.last_goals = new_goals
        print(f"[GoalSetter] Сгенерировано целей: {new_goals}")
        return new_goals
