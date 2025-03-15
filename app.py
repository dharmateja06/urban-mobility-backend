from flask import Flask, request, jsonify, render_template
from datetime import datetime
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Simulated in-memory database
rides_db = []
driver_demand_areas = ['Majestic', 'Electronic City', 'Koramangala']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book_ride', methods=['POST'])
def book_ride():
    data = request.json
    pickup = data.get('pickup')
    drop = data.get('drop')
    mode = data.get('mode')

    ride = {
        'id': len(rides_db) + 1,
        'pickup': pickup,
        'drop': drop,
        'mode': mode,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'status': 'Pending'
    }

    rides_db.append(ride)
    return jsonify({'message': 'Ride booked successfully!', 'ride': ride}), 200

@app.route('/get_demand_alerts', methods=['GET'])
def demand_alerts():
    return jsonify({'demand_areas': driver_demand_areas})

import os

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)