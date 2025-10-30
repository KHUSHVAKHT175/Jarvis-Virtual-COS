"""
main.py — Jarvis Virtual-COS с файлами, сетью, web и плагинами

Философия:
- Когнитивная архитектура: meta-слои 7D/11D/15D (смысловое управление)
- Прямой обмен с внешним миром: файлы, сети, webhooks и плагины
"""

import sys
import socket
import requests
from flask import Flask, request
import threading

# --- Meta-слои (как раньше) ---
from meta.field7d import Field7D_Intent
from meta.field11d import Field11D_TimeRewriter
from meta.field15d import Field15D_Core

class I1Stub:
    goal_mode = "normal"
    def restore_from_state(self, state):
        print(f"[I1] Реставрация состояния: {state}")
    def log(self, msg):
        print(f"[I1] {msg}")

class I2Stub:
    repair_mode = False
    errors = 0
    def log(self, msg):
        print(f"[I2] {msg}")

I1 = I1Stub()
I2 = I2Stub()

field7d = Field7D_Intent()
field11d = Field11D_TimeRewriter()
field15d = Field15D_Core([field7d, field11d])

# --- Файловый обмен (file_exchange) ---
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
    with open(COMMAND_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    open(COMMAND_FILE, 'w').close()
    return [line.strip() for line in lines if line.strip()]

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

# --- HTTP REST API (Flask) ---
api_app = Flask(__name__)

@api_app.route('/command', methods=['POST'])
def api_command():
    data = request.json
    print(f"[HTTP] Received: {data}")
    return {'status': 'ok'}

def run_http_api():
    api_app.run(port=5000)

# --- Веб-интерфейс (Flask) ---
web_panel = Flask(__name__)
LOGS = []

@web_panel.route('/')
def index():
    return "<br>".join(LOGS)

@web_panel.route('/send', methods=['POST'])
def send_command():
    cmd = request.form.get('command', '')
    LOGS.append(f"Received command: {cmd}")
    return "OK"

def run_web_panel():
    web_panel.run(port=8080)

# --- Telegram, Discord, Email уведомления ---
TOKEN = "TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
DISCORD_URL = "YOUR_DISCORD_WEBHOOK"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': message})

def send_discord(message):
    payload = {"content": message}
    requests.post(DISCORD_URL, json=payload)

# Для email — внедряется через smtplib отдельно (по требованию)

# --- Обработка stdin/stdout (потоковые команды) ---
def process_stdin():
    print("[STDIN] Ожидание команды...")
    command = sys.stdin.readline().strip()
    print(f"[STDIN] Processed: {command}")

# --- Основной цикл ОС ---
def main_loop():
    print("🧠 Jarvis Virtual-COS запущен с интеграцией файлов, сети и web!")
    print("--- Мета-уровни подключены: 7D, 11D, 15D ---")
    system_state = {"load": 0.82, "errors": 1}
    # Meta-смыслы
    field7d.sense(system_state)
    field7d.influence(I1, I2)
    field11d.record(system_state)
    field15d.evaluate()
    field15d.broadcast()
    # --- Пример работы с файлами ---
    write_file("hello.txt", "Привет, Jarvis!")
    msg = read_file("hello.txt")
    print(f"[FS] {msg}")
    append_file("hello.txt", "Еще строка.")
    print("[FS] Append ok.")
    # --- Очередь команд ---
    commands = fetch_commands()
    print(f"[FS] Commands from file: {commands}")
    # --- Внешние уведомления ---
    # send_telegram("Система стартовала!")  # раскомментируй если есть токен
    # send_discord("Система стартовала!")    # раскомментируй если есть url
    # --- Потоковый режим ---
    # process_stdin()                       # из консоли
    print("--- Основной цикл завершён ---")

if __name__ == "__main__":
    # --- Параллельный запуск сервисов
    threading.Thread(target=tcp_server, daemon=True).start()
    threading.Thread(target=run_http_api, daemon=True).start()
    threading.Thread(target=run_web_panel, daemon=True).start()
    main_loop()
