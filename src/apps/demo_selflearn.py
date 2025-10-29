class App:
    def __init__(self):
        self.name = "demo_selflearn"
        self.training_steps = []

    def run(self, task=None):
        if task:
            self.training_steps.append(task)
            print(f"[demo_selflearn] Выполнено обучение шаг: {task}")
        print("[demo_selflearn] Все шаги обучения:")
        for idx, ts in enumerate(self.training_steps):
            print(f"{idx+1}: {ts}")

    def status(self):
        return f"[demo_selflearn] Прошло шагов: {len(self.training_steps)}"

    def get_context(self):
        return {"name": self.name, "status": self.status(), "training_steps": self.training_steps}

if __name__ == "__main__":
    app = App()
    app.run("Тест нагрузки")
    app.run("Изменение параметров конфигурации")
    app.run()
