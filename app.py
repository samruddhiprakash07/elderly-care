from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import random

app = Flask(__name__)
CORS(app)  # This allows the React Dashboard to talk to this Python script

# Simulated databases
reminders = [
    {"time": "09:00", "task": "Take blood pressure medicine"},
    {"time": "13:00", "task": "Drink water"},
    {"time": "20:00", "task": "Evening walk"}
]

alerts = []
transactions = [
    {"date": "2026-04-01", "amount": 5000, "desc": "Electricity bill"},
    {"date": "2026-04-01", "amount": 20000, "desc": "Unusual transfer"}
]

@app.route("/reminders", methods=["GET"])
def get_reminders():
    now = datetime.datetime.now().strftime("%H:%M")
    # Sending all reminders so the dashboard isn't empty
    return jsonify({"current_time": now, "due_reminders": reminders})

@app.route("/fall_detected", methods=["POST"])
def fall_detected():
    alerts.append({"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "alert": "Fall detected!"})
    return jsonify({"status": "alert sent", "alerts": alerts})

@app.route("/alerts", methods=["GET"])
def get_alerts():
    return jsonify({"alerts": alerts})

@app.route("/health", methods=["GET"])
def health_monitor():
    heartbeat = random.randint(60, 120)
    bp_systolic = random.randint(100, 160)
    bp_diastolic = random.randint(60, 100)
    status = "Normal"
    if heartbeat > 110 or bp_systolic > 140:
        status = "Warning: abnormal vitals detected"
    return jsonify({
        "heartbeat": f"{heartbeat} bpm",
        "blood_pressure": f"{bp_systolic}/{bp_diastolic}",
        "status": status
    })

@app.route("/finance", methods=["GET"])
def finance_monitor():
    suspicious = [t for t in transactions if t["amount"] > 10000]
    return jsonify({
        "status": "Alert: unusual spending detected" if suspicious else "Normal"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    