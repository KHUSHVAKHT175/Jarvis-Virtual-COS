# src/core/auto_weights.py
def night_optimize_weights(memory):
    for name in memory.weights:
        if name in memory.archive:
            memory.weights[name] = max(1.0, memory.weights[name] - 0.2)
        else:
            memory.weights[name] = min(memory.weights[name] + 0.05, 10.0)
def update_weights(memory, reward=0.0, curiosity=0.0):
    base_factor = 0.1
    adjustment = base_factor * (reward + curiosity) / 2
    if not hasattr(memory, "weights"):
        memory.weights = {}
    memory.weights["motivation_bias"] = memory.weights.get("motivation_bias", 1.0) + adjustment
    print(f"[AutoWeights] Обновлены веса мотивации: +{adjustment:.3f}")