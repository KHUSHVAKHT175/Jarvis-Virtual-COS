class App:
    def __init__(self):
        self.name = "event"
        self.events = []

    def run(self, event=None):
        if event:
            self.events.append(event)
            print(f"[event] Получено событие: {event}")
        else:
            print(f"[event] Все события:")
            for idx, ev in enumerate(self.events):
                print(f"{idx+1}: {ev}")

    def status(self):
        return f"[event] Событий накоплено: {len(self.events)}"

    def get_context(self):
        return {"name": self.name, "status": self.status(), "events": self.events}

if __name__ == "__main__":
    app = App()
    app.run("Запуск автообновления")
    app.run()
