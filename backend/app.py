from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Get image from request
        image = request.files.get('image')
        if not image:
            return jsonify({"error": "No image provided"}), 400

        # Dummy response for now
        response = {
            "message": "Image received successfully",
            "insights": {
                "detected_items": ["apple", "banana peel"],
                "estimated_volume": "0.5 kg",
                "carbon_footprint": "0.7 kg CO2" 
            }
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)