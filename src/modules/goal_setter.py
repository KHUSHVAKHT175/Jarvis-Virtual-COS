import random
import time

class GoalSetter:
    def __init__(self):
        self.active_goals = []

    def generate_goals(self, curiosity_level, reward):
        """
        Генерация новых целей в зависимости от мотивационных параметров.
        Чем выше любопытство и награда — тем больше и разнообразнее цели.
        """
        print("[GoalSetter] Генерация целей...")
        goals = []

        # Если интерес и вознаграждение низкие — ставим цель на восстановление мотивации
        if curiosity_level < 0.3 and reward < 0.2:
            goals.append("анализ причин снижения мотивации")
            goals.append("поиск новых источников интереса")
        # Средний уровень — поддержка текущей активности
        elif 0.3 <= curiosity_level <= 0.7:
            goals.append("оптимизация текущих задач")
            goals.append("углубление анализа данных")
        # Высокий уровень — расширение возможностей
        else:
            goals.append("поиск новых направлений развития")
            goals.append("эксперимент с новыми параметрами")
            if random.random() > 0.5:
                goals.append("создание нового сценария взаимодействия")

        # фиксируем цели во внутреннем списке
        for g in goals:
            self.active_goals.append({
                "goal": g,
                "timestamp": time.time(),
                "status": "active"
            })

        print(f"[GoalSetter] Новые цели: {goals}")
        return goals
