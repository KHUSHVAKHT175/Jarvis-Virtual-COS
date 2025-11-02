# growth_module.py

def growth_step(memory, field7d, I1, I2):
    """
    Выполняет один цикл роста интеллекта,
    обновляет смысловое поле и даёт обратную связь.
    """
    recent_assoc = memory.assoc_last(10)  # Возьми последние 10 ассоциаций (пример)
    # Простая логика роста: увеличиваем энергию, если есть успех
    # Можно расширять, основываясь на реальных данных
    success = True
    if success:
        field7d.energy = min(field7d.energy + 0.05, 1.0)
    else:
        field7d.energy = max(field7d.energy - 0.02, 0.0)

    I1.set_goal("Рост интеллекта")
    I1.feedback("Рост успешно завершен", memory)
    I2.observe(I1.goal)

    return f"Рост завершен, энергия: {field7d.energy:.2f}"
