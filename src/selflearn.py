import json
import datetime
import random

class SelfLearner:
    """
    Простая система самообучения Jarvis — учится через отражение результата команд.
    """
    def __init__(self, path="selflearn.json"):
        self.path = path
        try:
            with open(self.path, encoding='utf-8') as f:
                self.data = json.load(f)
        except:
            self.data = {"sessions": []}

    def reflect(self, intent, result):
        """Фиксирует попытку, результат и успешность."""
        success = "ok" in str(result).lower() or "выполнена" in str(result).lower()
        entry = {
            "time": str(datetime.datetime.now()),
            "intent": intent,
            "result": str(result),
            "success": success,
            "weight": 1.0 if success else -0.5
        }
        self.data["sessions"].append(entry)
        self._save()
        print(f"[selflearn] Рефлексия: {intent} → {'успех' if success else 'ошибка'}")

    def _save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
    
    def summary(self):
        """Краткая сводка успешных и неуспешных действий."""
        success = len([x for x in self.data["sessions"] if x["success"]])
        fail = len(self.data["sessions"]) - success
        return {"успехи": success, "ошибки": fail}
