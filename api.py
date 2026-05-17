from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

DB_NAME = "data.db"

def query_db(code):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT expires_at, active FROM keys WHERE code = ?", (code,))
    row = cur.fetchone()
    conn.close()
    return row

@app.route("/validate", methods=["POST"])
def validate():
    payload = request.get_json()
    code = payload.get("code")

    row = query_db(code)

    if not row:
        return jsonify({"valid": False, "message": "Code not found"})

    expires_at, active = row

    if not active:
        return jsonify({"valid": False, "message": "Code disabled"})

    if datetime.now() > datetime.fromisoformat(expires_at):
        return jsonify({"valid": False, "message": "Expired"})

    return jsonify({"valid": True, "message": "Access granted"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)