# src/api_app.py
from flask import Flask, jsonify
from orchestrator import orchestrator_instance

app = Flask(__name__)

@app.route("/motivation_status")
def motivation_status():
    log = orchestrator_instance.memory.get("log", [])
    return jsonify(log[-10:])  # последние 10 записей
