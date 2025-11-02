# src/modules/reward_system.py
class RewardSystem:
    def evaluate(self, success=True):
        reward = 1.0 if success else -0.5
        print(f"[RewardSystem] → Вычислен reward = {reward}")
        return reward
