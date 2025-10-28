class App:
    def __init__(self):
        self.name = "settings"  # заменить на соответствующее имя для каждого файла

    def run(self, *args):
        print(f"App {self.name}: запуск с аргументами {args}")
        # здесь реализация функционала

    def status(self):
        return f"App {self.name}: готов к работе."

    def get_context(self):
        return {"name": self.name, "status": self.status()}

# Для теста "по месту":
if __name__ == "__main__":
    app = App()
    app.run()
    print(app.status())
    print(app.get_context())
