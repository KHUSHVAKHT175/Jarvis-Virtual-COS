class App:
    def __init__(self):
        self.name = "logview"
        self.logs = []

    def run(self, log=None):
        if log:
            self.logs.append(log)
            print(f"[logview] Добавлен лог: {log}")
        else:
            print(f"[logview] Просмотр логов:")
            for idx, l in enumerate(self.logs):
                print(f"{idx+1}: {l}")

    def status(self):
        return f"[logview] Логов накоплено: {len(self.logs)}"

    def get_context(self):
        return {"name": self.name, "status": self.status(), "logs": self.logs}

if __name__ == "__main__":
    app = App()
    app.run("Ошибка ядра Layer-2")
    app.run()
