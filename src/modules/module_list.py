# src/modules/module_list.py

# Убираем все 'core.*', оставляем только реально существующие модули
module_registry = {
    "AutoWeights": "modules.auto_weights",
    "NightOptimizer": "modules.night_optimizer",
    # другие реальные модули
}