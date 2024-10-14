from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')  # Renders the main HTML page

# Endpoint to get the pH value as JSON (for AJAX request)
@app.route('/get-ph', methods=['GET'])
def get_ph():
    ph_value = simulate_ph_check()  # Get the simulated pH value
    return jsonify({"ph_value": ph_value})

# Function to simulate the pH value (you can replace this with actual sensor data)
def simulate_ph_check():
    ph_value = 5.0 + time.time() % 10 * 0.4  # Simulated changing pH values
    return round(ph_value, 2)

if __name__ == '__main__':
    app.run(debug=True)
