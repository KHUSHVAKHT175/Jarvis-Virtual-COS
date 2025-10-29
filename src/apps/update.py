class App:
    def __init__(self):
        self.name = "update"
        self.updated = False

    def run(self):
        self.updated = True
        print("[update] Обновление системы завершено.")

    def status(self):
        return "[update] Статус: Обновлено." if self.updated else "[update] Статус: Требуется обновление."

    def get_context(self):
        return {"name": self.name, "status": self.status(), "updated": self.updated}

if __name__ == "__main__":
    app = App()
    app.run()
    print(app.status())
