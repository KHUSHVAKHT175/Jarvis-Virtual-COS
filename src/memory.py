# -*- coding: utf-8 -*-
import json
import os

class IntentMemory:
    """
    IntentMemory — внутренняя память смыслов и ассоциаций Jarvis Virtual-COS.
    Хранит намерения (intent), контекст и позволяет получать последние связи.
    """

    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self._load()

    # --- Загрузка из файла ---
    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                try:
                    self.data = json.load(f)
                except Exception:
                    self.data = []
        else:
            self.data = []

    # --- Сохранение в файл ---
    def _save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    # --- Добавление новой записи ---
    def add(self, intent, context=None):
        record = {"intent": intent, "context": context or {}}
        self.data.append(record)
        self._save()

    # --- Последний элемент ---
    def get_last(self):
        if self.data:
            return self.data[-1]
        return None

    # --- Все записи ---
    def all(self):
        return self.data

    # --- Ассоциативный список последних n записей ---
    def assoc_last(self, n=6):
        """
        Возвращает последние n элементов в виде пар (intent → context)
        для визуализации в веб-панели Jarvis Virtual-COS.
        """
        if not self.data:
            return []
        items = []
        for item in self.data[-n:]:
            intent = item.get("intent", "")
            context = item.get("context", {})
            items.append((intent, context))
        return items
        # --- Добавление ассоциативной связи ---
    def associate(self, key, value):
        """
        Добавляет простую ассоциативную связь в память (используется веб-интерфейсом).
        Например: associate('hello', {'console': True})
        """
        self.data.append({"assoc": {key: value}})
        self._save()
