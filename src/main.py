"""
main.py — Jarvis Virtual-COS: живой цикл, intent_memory, самообучение, web-интерфейс с интерактивом и логом.

Философия:
- Meta-слои, память, цели, ошибки — смысловое ядро Jarvis
- Самообучение через отражение: поле 7D регулирует энергию смыслов
- Web-панель — органическое окно сознания: все действия, цели, состояния видны и доступны
"""

import sys
import socket
import requests
from flask import Flask, request, render_template_string
import threading
from time import sleep, time, strftime

# --- Внутренние сервисы ---
from memory import IntentMemory
from interface import UserInterface

# --- Meta-слои ---
from meta.field7d import Field7D_Intent
from meta.field11d import Field11D_TimeRewriter
from meta.field15d import Field15D_Core

# --- I1/I2 с реальной петлёй обратной связи ---
class I1Stub:
    goal = "Ожидание команды"
    def set_goal(self, g):
        self.goal = g
    def feedback(self, errors):
        print(f"[I1] Получен фидбек от I2: ошибок {errors}")

class I2Stub:
    errors = 0
    def add_error(self): self.errors += 1
    def observe(self, goal):
        print(f"[I2] Наблюдает за целью I1: {goal}")

I1 = I1Stub()
I2 = I2Stub()

# --- Meta-поля ---
field7d = Field7D_Intent()
field11d = Field11D_TimeRewriter()
field15d = Field15D_Core([field7d, field11d])

# --- Энергия смыслов 7D ---
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
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def append_file(path, content):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content + '\n')

COMMAND_FILE = "commands.txt"
def fetch_commands():
    try:
        with open(COMMAND_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        open(COMMAND_FILE, 'w').close()
        return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        return []

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

# --- Web-панель: интерактивная форма, лог, heartbeat, цели/ошибки ---
web_panel = Flask(__name__)
LOGS = []
HEARTBEAT = {"last": time(), "count": 0}
ENERGY_7D = [0.5]

@web_panel.route('/', methods=['GET', 'POST'])
def home():
    pulse = f"Пульс ядра: {strftime('%H:%M:%S')} | Цикл: {HEARTBEAT['count']}"
    energy = f"{getattr(field7d, 'energy', 0.5):.2f}"
    msg = ""
    if request.method == 'POST':
        cmd = request.form.get('command', '').strip()
        if cmd:
            LOGS.append(f">>> {cmd}")
            I1.set_goal(f"Выполняем: {cmd}")
            result = f"ok (web)"  # Здесь имитируем результат, можно расширить
            memory.add(cmd)
            adapt_7d(field7d, cmd, result)
            LOGS.append(f"[web] {result} | Энергия смыслов: {energy}")
            I1.feedback(I2.errors)
            I2.observe(I1.goal)
            msg = f"Выполнена команда: {cmd}"
    log_html = "<br>".join(LOGS[-30:])
    html = f"""
    <h1>Jarvis Virtual-COS</h1>
    <form method="post">
        <input name="command" placeholder="Ввести команду" autofocus>
        <button type="submit">Отправить</button>
    </form>
    <p>{pulse} | Энергия смыслов (7D): <b>{energy}</b></p>
    <p>Текущая цель (I1): {I1.goal}</p>
    <p>Ошибок (I2): {I2.errors}</p>
    <div style='font-family:monospace;background:#eee;padding:12px;margin:1em 0;border-radius:6px;max-height:35vh;overflow:auto'>{log_html}</div>
    <small>Jarvis живёт — обнови страницу, видно “пульс” и эволюцию!</small>
    <p style="color:green">{msg}</p>
    """
    return html

def run_web_panel():
    web_panel.run(port=8080)

# --- Telegram и Discord уведомления (по желанию) ---
TOKEN = "TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
DISCORD_URL = "YOUR_DISCORD_WEBHOOK"
def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': message})
def send_discord(message):
    payload = {"content": message}
    requests.post(DISCORD_URL, json=payload)

# --- Основной "живой" цикл ОС со смысловой регуляцией ---
def core_loop():
    global memory
    memory = IntentMemory("memory.json")
    ui = UserInterface(log_ref=LOGS)
    print("\n🧠 Jarvis Virtual-COS запущен и ждёт команд!")
    print("--- Мета-уровни подключены: 7D, 11D, 15D ---")
    print("Для выхода — нажмите Stop (прервать выполнение скрипта)\n")
    system_state = {"load": 0.82, "errors": 1}
    field7d.sense(system_state)
    field7d.influence(I1, I2)
    field11d.record(system_state)
    field15d.evaluate()
    field15d.broadcast()
    write_file("hello.txt", "Привет, Jarvis!")
    append_file("hello.txt", "Еще строка.")

    try:
        while True:
            cmd = ui.get_command()
            file_cmds = fetch_commands()
            if not cmd and file_cmds:
                cmd = file_cmds[0]
            result = None
            if cmd:
                memory.add(cmd)
                I1.set_goal(f"Выполняем: {cmd}")
                result = ui.process(cmd, memory)
                adapt_7d(field7d, cmd, result)
                ui.respond(result)
                LOGS.append(f"[main] {result} | Энергия смыслов: {getattr(field7d,'energy',0.5):.2f}")
                I1.feedback(I2.errors)
                I2.observe(I1.goal)
            HEARTBEAT["count"] += 1
            HEARTBEAT["last"] = time()
            sleep(0.2)
    except KeyboardInterrupt:
        print("\nJarvis остановлен. Сессия завершена.")

if __name__ == "__main__":
    threading.Thread(target=tcp_server, daemon=True).start()
    threading.Thread(target=run_http_api, daemon=True).start()
    threading.Thread(target=run_web_panel, daemon=True).start()
    core_loop()
