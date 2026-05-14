from flask import Flask, jsonify, request
import os
import time
import math
import random
from datetime import datetime, timezone

app = Flask(__name__)
START_TIME = time.time()
APP_NAME = os.getenv("APP_NAME", "Servicio Demo")

@app.route("/")
def index():
    return jsonify({
        "service": APP_NAME,
        "message": "Aplicación Python para laboratorio de observabilidad con Zabbix y Grafana",
        "endpoints": ["/health", "/api/orders", "/cpu?seconds=5", "/error"]
    })

@app.route("/health")
def health():
    uptime = round(time.time() - START_TIME, 2)
    return jsonify({
        "status": "ok",
        "service": APP_NAME,
        "uptime_seconds": uptime,
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route("/api/orders")
def orders():
    data = [
        {"id": i, "course": random.choice(["Sistemas Operativos", "Redes", "Cloud", "DevOps"]), "status": random.choice(["ok", "pending", "warning"])}
        for i in range(1, 6)
    ]
    return jsonify({"items": data, "total": len(data)})

@app.route("/cpu")
def cpu_load():
    seconds = int(request.args.get("seconds", 5))
    seconds = max(1, min(seconds, 30))
    end = time.time() + seconds
    x = 0.0
    while time.time() < end:
        x += math.sqrt(random.random())
    return jsonify({"status": "load_generated", "seconds": seconds, "value": x})

@app.route("/error")
def error():
    return jsonify({"status": "error", "message": "Error simulado para probar monitoreo"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
