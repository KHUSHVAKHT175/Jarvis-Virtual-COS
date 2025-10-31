import json
import os

class IntentMemory:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self._load()

    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                try:
                    self.data = json.load(f)
                except Exception:
                    self.data = []
        else:
            self.data = []

    def add(self, intent, context=None):
        record = {"intent": intent, "context": context or {}}
        self.data.append(record)
        self._save()

    def _save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def get_last(self):
        if self.data:
            return self.data[-1]
        return None

    def all(self):
        return self.data
