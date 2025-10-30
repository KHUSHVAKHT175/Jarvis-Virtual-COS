class Plugin:
    def __init__(self, name):
        self.name = name

    def run(self, data):
        # логика плагина
        return f"{self.name} processed {data}"
