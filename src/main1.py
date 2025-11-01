# -*- coding: utf-8 -*-
"""
main1.py — Jarvis Virtual-COS: альтернативный когнитивный контур с веб-панелью.
Тренировочный режим для Field7D, IntentMemory и I1/I2.

Цель: тест быстрой интерактивной обратной связи и адаптации смыслов через web-интерфейс.
"""

import sys
import socket
from flask import Flask, request
import threading
from time import sleep, time, strftime

# --- Внутренние сервисы ---
from memory import IntentMemory
from interface import UserInterface

# --- Meta-слои ---
from meta.field7d import Field7D_Intent
from meta.field11d import Field11D_TimeRewriter
from meta.field15d import Field15D_Core

# --- Когнитивные узлы ---
class I1Stub:
    def __init__(self):
        self.goal = "Ожидание команды"
    def set_goal(self, g):
        self.goal = g
    def feedback(self, fact, memory):
        memory.associate(self.goal, fact)
        print(f"[I1] Feedback: {self.goal} <-> {fact}")

class I2Stub:
    def __init__(self):
        self.errors = 0
    def add_error(self):
        self.errors += 1
    def observe(self, goal):
        print(f"[I2] Observe I1 goal: {goal}")

I1 = I1Stub()
I2 = I2Stub()

# --- Поля ---
field7d = Field7D_Intent()
field11d = Field11D_TimeRewriter()
field15d = Field15D_Core([field7d, field11d])

# --- Адаптация поля 7D ---
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

# --- TCP сервер ---
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

# --- Web панель ---
web_panel = Flask(__name__)
LOGS = []
HEARTBEAT = {"last": time(), "count": 0}
memory = IntentMemory("memory.json")

@web_panel.route('/', methods=['GET', 'POST'])
def home():
    pulse = f"Пульс: {strftime('%H:%M:%S')} | Цикл: {HEARTBEAT['count']}"
    energy = f"{getattr(field7d, 'energy', 0.5):.2f}"
    assoc_text = "<ul>" + "".join(f"<li><b>{k}</b> → {v}</li>" for k, v in list(memory.assoc_last(6))) + "</ul>"
    msg = ""
    if request.method == 'POST':
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
    <html>
    <head><meta charset="utf-8"><title>Jarvis Virtual-COS</title></head>
    <body style='font-family:Arial, sans-serif'>
    <h1>Jarvis Virtual-COS</h1>
    <form method="post">
        <input name="command" placeholder="Ввести команду" autofocus>
        <button type="submit">Отправить</button>
    </form>
    <p>{pulse} | Энергия смыслов (7D): <b>{energy}</b></p>
    <p>Текущая цель (I1): {I1.goal}</p>
    <p>Ошибок (I2): {I2.errors}</p>
    <h3>Ассоциативные связи памяти (последние):</h3>{assoc_text}
    <div style='font-family:monospace;background:#eee;padding:12px;margin:1em 0;
    border-radius:6px;max-height:35vh;overflow:auto'>{log_html}</div>
    <small>Jarvis саморазвивается — обнови страницу: пульс, память, сознание!</small>
    <p style="color:green">{msg}</p>
    </body>
    </html>
    """
    return html

def run_web_panel():
    web_panel.run(port=8080)

# --- Основной цикл ---
def core_loop():
    ui = UserInterface(log_ref=LOGS)
    print("\n🧠 Jarvis Virtual-COS: когнитивный цикл жизни и самообучения!")
    print("--- Многоуровневая память, meta-уровни, ассоциации, пульс ---")
    while True:
        try:
            cmd = ui.get_command()
            if cmd:
                memory.add(cmd, context={"console": True})
                I1.set_goal(f"Выполняем: {cmd}")
                result = ui.process(cmd, memory)
                adapt_7d(field7d, cmd, result)
                I1.feedback(result, memory)
                I2.observe(I1.goal)
                LOGS.append(f"[main] {result} | Энергия смыслов: {getattr(field7d, 'energy',0.5):.2f}")
            HEARTBEAT["count"] += 1
            HEARTBEAT["last"] = time()
            sleep(0.3)
        except KeyboardInterrupt:
            print("\nJarvis остановлен. Сессия завершена.")
            break

if __name__ == "__main__":
    threading.Thread(target=tcp_server, daemon=True).start()
    threading.Thread(target=run_web_panel, daemon=True).start()
    core_loop()
