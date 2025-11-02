class RewardSystem:
    def __init__(self):
        self.total_reward = 0.0

    def evaluate(self, success=True):
        """
        Возвращает числовую оценку успеха.
        """
        reward = 1.0 if success else -0.5
        self.total_reward += reward
        print(f"[RewardSystem] Текущая общая награда: {self.total_reward}")
        return reward
