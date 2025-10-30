class Field11D_TimeRewriter:
    def __init__(self):
        self.timeline = []

    def record(self, state):
        # Сохраняем "срез" состояния системы
        self.timeline.append(state.copy())

    def rewind(self, steps=1):
        # Откат состояния назад по истории
        if len(self.timeline) >= steps:
            return self.timeline[-steps]
        return None

    def rewrite(self, I1, I2):
        # По ошибкам — откатить план I1 во времени
        if hasattr(I2, "errors") and I2.errors > 3:
            restored = self.rewind(2)
            if restored and hasattr(I1, "restore_from_state"):
                I1.restore_from_state(restored)
                if hasattr(I1, 'log'):
                    I1.log("[11D] State rewound due to errors.")
