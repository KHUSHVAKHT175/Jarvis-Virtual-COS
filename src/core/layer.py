class Layer:
    def __init__(self, name, inner_layer=None, params=None):
        self.name = name
        self.inner_layer = inner_layer  # вложенный слой (или None)
        self.params = params or {}
        self.context = {}
        self.memory_sandbox = {}
        self.state = 'initialized'

    def init(self, params=None):
        if params:
            self.params.update(params)
        self.state = 'initialized'

    def run(self, input_data=None):
        self.state = 'running'
        self.context['input'] = input_data
        result = self.process(input_data)
        if self.inner_layer:
            return self.inner_layer.run(result)
        return result

    def process(self, data):
        # Базовая логика слоя; перегрузи в наследниках
        return data

    def freeze(self):
        self.state = 'frozen'

    def migrate(self, new_params):
        self.params.update(new_params)
        self.state = 'migrated'

    def snapshot(self):
        return {
            "name": self.name,
            "params": self.params,
            "context": self.context,
            "memory": self.memory_sandbox,
            "state": self.state
        }

    def restore(self, snapshot):
        self.name = snapshot.get("name", self.name)
        self.params = snapshot.get("params", {})
        self.context = snapshot.get("context", {})
        self.memory_sandbox = snapshot.get("memory", {})
        self.state = snapshot.get("state", "initialized")

    def destroy(self):
        self.state = 'destroyed'
        self.inner_layer = None
        self.context.clear()
        self.memory_sandbox.clear()
