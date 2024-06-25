from flask import Flask, request, jsonify

app = Flask(__name__)

# Threshold temperature for the warning
TEMP_THRESHOLD = 25

@app.route("/temperature", methods=["POST"])
def temperature():
    """An endpoint accepting a temperature reading"""

    data = request.json  # temperature reading

    # Log de ontvangen temperatuur
    temperature = data.get('temperature')
    print("Ontvangen temperatuur:", temperature)

    # Check if temperature exceeds the threshold
    if temperature is not None and temperature > TEMP_THRESHOLD:
        response = {
            'message': 'Temperature exceeds threshold. Set the red LED.',
            'set_red_led': True
        }
    else:
        response = {
            'message': 'Temperature is normal.',
            'set_red_led': False
        }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
