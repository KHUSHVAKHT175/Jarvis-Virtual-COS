class App:
    def __init__(self):
        self.name = "sync"
        self.synced = False

    def run(self):
        self.synced = True
        print("[sync] Система синхронизирована.")

    def status(self):
        return "[sync] Статус: Синхронизирован." if self.synced else "[sync] Статус: Ожидание синхронизации."

    def get_context(self):
        return {"name": self.name, "status": self.status(), "synced": self.synced}

if __name__ == "__main__":
    app = App()
    app.run()
    print(app.status())
