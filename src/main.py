"""
main.py — Jarvis Virtual-COS: глубокий когнитивный цикл, многоуровневая память, интерактивная web-панель

Философия: meta-слои, ассоциативное поле памяти, петля намерения и самообучающая коррекция, мгновенность реакции
"""

import sys
import socket
import requests
from flask import Flask, request
import threading
from time import sleep, time, strftime

# --- Внутренние сервисы (IntentMemory, UserInterface, SelfLearner) ---
from memory import IntentMemory
from interface import UserInterface

# --- Meta-слои ---
from meta.field7d import Field7D_Intent
from meta.field11d import Field11D_TimeRewriter
from meta.field15d import Field15D_Core

# --- Когнитивные слои ---
class I1Stub:
    def __init__(self): self.goal = "Ожидание команды"
    def set_goal(self, g): self.goal = g
    def feedback(self, fact, memory):
        memory.associate(self.goal, fact)
        print(f"[I1] Feedback: {self.goal} <-> {fact}")

class I2Stub:
    def __init__(self): self.errors = 0
    def add_error(self): self.errors += 1
    def observe(self, goal): print(f"[I2] Observe I1 goal: {goal}")

I1 = I1Stub()
I2 = I2Stub()

field7d = Field7D_Intent()
field11d = Field11D_TimeRewriter()
field15d = Field15D_Core([field7d, field11d])

def adapt_7d(field, intent, result):
    success = "ok" in str(result).lower() or "успех" in str(result).lower()
    field.energy = getattr(field, "energy", 0.5)
    old_energy = field.energy
    if success:
        field.energy += 0.02
    else:
        field.energy -= 0.01
    field.energy = max(0, min(field.energy, 1))
    print(f"[7D] Энергия смыслового поля: {old_energy:.2f} → {field.energy:.2f}")

# --- Файловый обмен ---
def read_file(path):
    with open(path, 'r', encoding='utf-8') as f: return f.read()
def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f: f.write(content)
def append_file(path, content):
    with open(path, 'a', encoding='utf-8') as f: f.write(content + '\n')
COMMAND_FILE = "commands.txt"
def fetch_commands():
    try:
        with open(COMMAND_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        open(COMMAND_FILE, 'w').close()
        return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError: return []

# --- TCP-сервер ---
def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 9000))
    s.listen(5)
    print("[TCP] server running on port 9000...")
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024).decode()
        print(f"[TCP] Received: {data}")
        conn.send(b'Command received')
        conn.close()

# --- HTTP REST API ---
api_app = Flask("api_app")
@api_app.route('/command', methods=['POST'])
def api_command():
    data = request.json
    print(f"[HTTP] Received: {data}")
    return {'status': 'ok'}
def run_http_api():
    api_app.run(port=5000)

# --- Веб-панель: интерактивная форма, лог, цели, ассоциативная память, смысловое поле ---
web_panel = Flask(__name__)
LOGS = []
HEARTBEAT = {"last": time(), "count": 0}
memory = IntentMemory("memory.json")

@web_panel.route('/', methods=['GET', 'POST'])
def home():
    pulse = f"Пульс: {strftime('%H:%M:%S')} | Цикл: {HEARTBEAT['count']}"
    energy = f"{getattr(field7d, 'energy', 0.5):.2f}"
    assoc_text = "<ul>" + "".join(f"<li><b>{k}</b> → {v}" for k,v in list(memory.assoc_last(6))) + "</ul>"
    msg = ""

    if request.method == 'POST':
        action = request.form.get('action')
        if action == "train_batch":
            batch_commands = [
                "снизить шум восприятия",
                "увеличить плотность смыслов",
                "создать ассоциацию на основе контекста",
                "анализировать последние N ассоциаций",
                "поиск паттернов",
                "установить цель X",
                "оценить цель",
                "выполнить цель"
            ]
            for cmd in batch_commands:
                LOGS.append(f">>> {cmd} (batch)")
                I1.set_goal(f"Выполняем: {cmd}")
                result = "ok (batch)"
                memory.add(cmd, context={"batch": True})
                adapt_7d(field7d, cmd, result)
                I1.feedback(result, memory)
                I2.observe(I1.goal)
                LOGS.append(f"[batch] {result} | Энергия смыслов: {getattr(field7d, 'energy',0.5):.2f}")
            msg = "[web] Папуас успешно обучен пакетом команд!"
        else:
            cmd = request.form.get('command', '').strip()
            if cmd:
                LOGS.append(f">>> {cmd}")
                I1.set_goal(f"Выполняем: {cmd}")
                result = "ok (web)"
                memory.add(cmd, context={"web": True})
                adapt_7d(field7d, cmd, result)
                I1.feedback(result, memory)
                I2.observe(I1.goal)
                msg = f"[web] Выполнена: {cmd}"
                LOGS.append(f"[web] {result} | Энергия смыслов: {energy}")

    log_html = "<br>".join(LOGS[-26:])
    html = f"""
    <h2>Конструктор запросов</h2>
    <form method="post" action="/">
      <label for="action">Действие:</label>
      <select name="action_type" id="action" required>
      <option value="">Выберите...</option>
      <option value="status">Показать статус</option>
      <option value="set_goal">Установить цель</option>
      <option value="associate">Создать ассоциацию</option>
      <option value="analyze">Анализ темы</option>
      <option value="clear">Очистить сессию</option>
      <option value="help">Помощь</option>
      </select><br><br>

      <label for="topic">Тема (если применимо):</label>
      <input type="text" id="topic" name="topic" placeholder="Введите тему"><br><br>

      <button type="submit" name="submit" value="build_request">Применить</button>
    </form>
    <h1>Jarvis Virtual-COS</h1>
    <form method="post">
        <input name="command" placeholder="Ввести команду" autofocus>
        <button type="submit" name="action" value="execute_command">Отправить</button>
        <button type="submit" name="action" value="train_batch">Обучить Папуаса</button>
    </form>
    <p>{pulse} | Энергия смыслов (7D): <b>{energy}</b></p>
    <p>Текущая цель (I1): {I1.goal}</p>
    <p>Ошибок (I2): {I2.errors}</p>
    <h3>Ассоциативные связи памяти (последние):</h3>{assoc_text}
    <div style='font-family:monospace;background:#eee;padding:12px;margin:1em 0;border-radius:6px;max-height:35vh;overflow:auto'>{log_html}</div>
    <small>Jarvis саморазвивается — обнови страницу: пульс, память, сознание!</small>
    <p style="color:green">{msg}</p>
    """
    return html

def heartbeat_loop():
    while True:
        HEARTBEAT['count'] += 1
        HEARTBEAT['last'] = time()
        sleep(5)

if __name__ == "__main__":
    threading.Thread(target=tcp_server, daemon=True).start()
    threading.Thread(target=run_http_api, daemon=True).start()
    threading.Thread(target=heartbeat_loop, daemon=True).start()
    web_panel.run(port=8000)
