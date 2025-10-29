class App:
    def __init__(self):
        self.name = "settings"
        self.config = {"max_load":0.8, "snapshot_freq":5}

    def run(self, key=None, value=None):
        if key and value is not None:
            self.config[key] = value
            print(f"[settings] Параметр {key} изменён на {value}")
        print(f"[settings] Текущий конфиг: {self.config}")

    def status(self):
        return f"[settings] Текущие параметры: {self.config}"

    def get_context(self):
        return {"name": self.name, "status": self.status(), "config": self.config}

if __name__ == "__main__":
    app = App()
    app.run("max_load",0.6)
    app.run()
