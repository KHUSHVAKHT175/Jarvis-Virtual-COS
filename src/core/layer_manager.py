class LayerManager:
    def __init__(self):
        self.layers = []
        self.state_log = []
        self.max_load = 0.8
        self.layer_status = {}

    def add_layer(self, layer):
        self.layers.append(layer)
        self.layer_status[layer.name] = {"active": True, "errors": 0}

    def check_system_load(self):
        import random
        load = random.uniform(0.0, 1.0)
        return load

    def adaptive_select_layers(self):
        load = self.check_system_load()
        if load > self.max_load:
            for layer in self.layers:
                if self.layer_status[layer.name]["active"]:
                    self.layer_status[layer.name]["active"] = False
                    self.state_log.append(f"ОС: Перегрузка! Выключен слой {layer.name}")
                    break
        else:
            for layer in self.layers:
                self.layer_status[layer.name]["active"] = True

    def run_all(self, input_data):
        results = []
        self.adaptive_select_layers()
        for layer in self.layers:
            if self.layer_status[layer.name]["active"]:
                try:
                    result = layer.process(input_data)
                    results.append(result)
                except Exception as e:
                    self.layer_status[layer.name]["errors"] += 1
                    self.state_log.append(f"Ошибка слоя {layer.name}: {str(e)}")
            else:
                self.state_log.append(f"Слой {layer.name} приостановлен.")
        return results if len(results) > 1 else results[0]

    def snapshot_all(self):
        return [
            {"name": layer.name, "active": self.layer_status[layer.name]["active"],
             "errors": self.layer_status[layer.name]["errors"], "state": "running" if self.layer_status[layer.name]["active"] else "paused"}
            for layer in self.layers
        ] + self.state_log
