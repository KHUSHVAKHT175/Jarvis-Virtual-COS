class App:
    def __init__(self):
        self.name = "monitor"
        self.stats = {}

    def run(self, stats):
        print(f"[monitor] Сбор статистики: {stats}")
        self.stats.update(stats)
        print(f"[monitor] Актуальные метрики: {self.stats}")

    def status(self):
        return f"[monitor] Мониторинг активен, {len(self.stats)} метрик."

    def get_context(self):
        return {"name": self.name, "status": self.status(), "stats": self.stats}

if __name__ == "__main__":
    app = App()
    app.run({"load":0.5, "errors":2})
    print(app.status())
