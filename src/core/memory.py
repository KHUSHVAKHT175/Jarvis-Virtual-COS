# src/core/memory.py

class HybridMemory:
    def __init__(self):
        self.cache = {}
        self.archive = {}

        # --- Новые поля мотивации ---
        self.weights = {}
        self.motivation_state = {
            "reward_history": [],
            "curiosity_history": [],
            "goal_history": [],
            "progress_log": [],
            "motivation_bias": 1.0
        }

    def store(self, task, result):
        self.cache[task["name"]] = result
        if len(self.cache) > 10:
            key, val = self.cache.popitem()
            self.archive[key] = val

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        if key in self.archive:
            return self.archive[key]
        return None

    # --- Методы для логирования мотивации ---
    def log_reward(self, reward):
        self.motivation_state["reward_history"].append(reward)
        if len(self.motivation_state["reward_history"]) > 1000:
            self.motivation_state["reward_history"].pop(0)

    def log_curiosity(self, curiosity):
        self.motivation_state["curiosity_history"].append(curiosity)
        if len(self.motivation_state["curiosity_history"]) > 1000:
            self.motivation_state["curiosity_history"].pop(0)

    def log_goal(self, goal):
        self.motivation_state["goal_history"].append(goal)

    def log_progress(self, note):
        self.motivation_state["progress_log"].append(note)

    def get_recent_motivation_summary(self):
        rewards = self.motivation_state["reward_history"]
        curiosity = self.motivation_state["curiosity_history"]
        return {
            "reward_avg": sum(rewards[-10:]) / 10 if rewards else 0,
            "curiosity_avg": sum(curiosity[-10:]) / 10 if curiosity else 0,
            "goals_count": len(self.motivation_state["goal_history"]),
        }

