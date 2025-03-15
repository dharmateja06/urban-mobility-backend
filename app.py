from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(_name_)
CORS(app)

# ----------------- Test Route -----------------
@app.route('/')
def home():
    return "✅ Hello! Flask Backend is Running Successfully on Render!"

@app.route('/api/test')
def test():
    return jsonify({"message": "Test API working fine!"})

# --------------- Add more routes below this if needed -----------------
# Example:
# @app.route('/api/data')
# def data():
#     return jsonify({"status": "success", "data": []})

# ------------------ Main Entry Point ------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Render's dynamic port
    app.run(host="0.0.0.0", port=port)