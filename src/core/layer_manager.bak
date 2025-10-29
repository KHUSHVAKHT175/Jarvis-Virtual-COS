from .layer import Layer

class LayerManager:
    def __init__(self):
        self.layers = []

    def add_layer(self, layer: Layer):
        self.layers.append(layer)

    def run_all(self, input_data=None):
        data = input_data
        for layer in reversed(self.layers):  # внешний к внутреннему
            data = layer.run(data)
        return data

    def get_layer(self, name):
        for layer in self.layers:
            if layer.name == name:
                return layer
        return None

    def migrate_layer(self, name, new_params):
        layer = self.get_layer(name)
        if layer:
            layer.migrate(new_params)

    def hot_swap(self, name, new_layer):
        for i, layer in enumerate(self.layers):
            if layer.name == name:
                self.layers[i] = new_layer

    def snapshot_all(self):
        return [layer.snapshot() for layer in self.layers]

    def restore_all(self, snapshots):
        for layer, snap in zip(self.layers, snapshots):
            layer.restore(snap)
