import importlib
import os

class AppManager:
    def __init__(self, app_dir="src.apps"):
        self.app_dir = app_dir
        self.apps = {}

    def discover_apps(self):
        app_path = os.path.join("src", "apps")
        for f in os.listdir(app_path):
            if f.endswith(".py"):
                app_name = f.replace(".py", "")
                try:
                    module = importlib.import_module(f"src.apps.{app_name}")
                    app_class = getattr(module, "App")
                    self.apps[app_name] = app_class()
                except Exception as e:
                    print(f"Ошибка загрузки приложения {app_name}: {str(e)}")

    def run_app(self, app_name, *args):
        if app_name in self.apps:
            return self.apps[app_name].run(*args)
        else:
            print(f"Программа {app_name} не найдена!")

    def status(self, app_name):
        if app_name in self.apps:
            return self.apps[app_name].status()
        else:
            return "Нет такого приложения."

    def list_apps(self):
        return list(self.apps.keys())
