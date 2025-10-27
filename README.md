# ?? Jarvis-COS Minimal
> Минималистская версия искусственного интеллекта Jarvis-COS, предназначенная для локального запуска, обучения и расширения.

## Quick Start

### Шаг 1: Клонирование репозитория
```bash
git clone https://github.com/KHUSHVAKHT175/Jarvis-COS.git
cd Jarvis-COS-Minimal
Шаг 2: Установка зависимостей

pip install -r requirements.txt
Шаг 3: Запуск основной программы

python src/main.py
Пример вывода в терминале
csharp

[INFO] Jarvis-COS initialized.
[INFO] Loading core modules...
[INFO] System ready. Awaiting commands.
Ключевые файлы и назначение
Путь / Файл	Назначение
src/main.py	Точка входа, управление модулями
src/core/process_core.py	Управление процессами
src/core/memory_engine.py	Память и обработка данных
src/core/command_parser.py	Разбор команд
src/core/scheduler.py	Планировщик задач
src/core/security_shell.py	Безопасность
src/core/system_log.py	Логирование
src/modules/dialog_engine.py	Диалог с пользователем
src/modules/logic_i1i2.py	Логика, мышление
src/modules/field_engine.py	Поле восприятия (stub)
src/modules/intuition_layer.py	Интуиция (stub)
src/modules/vision_adapter.py	Обработка визуальных данных
tests/test_core.py	Модуль тестов

Тестирование
Запуск тестов

pytest tests/test_core.py
Ожидаемый результат
============================= test session starts =============================
collected 5 items

tests/test_core.py .....                                                  [100%]

============================== 5 passed in 0.12s ==============================
FAQ
Как добавить новый модуль?
Создайте файл в папке src/modules/.

Добавьте регистрацию модуля в src/main.py или src/core/process_core.py.

Как сделать pull-request?
Форкните репозиторий.

Создайте новую ветку: git checkout -b feature/имя_фичи

Сделайте коммиты и пуш: git push origin feature/имя_фичи

Создайте Pull Request через GitHub.

Куда писать баги/предложения?
Используйте раздел Issues на GitHub.


cd Jarvis-COS
pip install -r requirements.txt
python src/main.py
```
--- 
## ?? Project Structure
--- 
## ?? Example Commands
```bash
Jarvis-COS
Jarvis-COS
Jarvis-COS
Jarvis-COS
```
--- 
## ?? Requirements
- Python 3.9+
- Git
- pip
--- 
## ?? License
MIT License c KHUSHVAKHT
