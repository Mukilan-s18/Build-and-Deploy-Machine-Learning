from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Load model pipeline
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')
if not os.path.exists(MODEL_PATH):
    # Fallback to models directory if running from project root
    MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'best_house_price_model.pkl')

model = joblib.load(MODEL_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'House Price Prediction API'})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        # Parse and validate inputs
        num_rooms = float(data.get('num_rooms', 3))
        num_bathrooms = float(data.get('num_bathrooms', 2))
        area_sqft = float(data.get('area_sqft', 1800))
        location = str(data.get('location', 'Suburbs'))
        age_years = float(data.get('age_years', 10))
        has_garage = int(data.get('has_garage', 1))

        # Engineer features identical to training pipeline
        total_rooms = num_rooms + num_bathrooms
        room_to_area_ratio = num_rooms / area_sqft if area_sqft > 0 else 0

        input_df = pd.DataFrame([{
            'num_rooms': num_rooms,
            'num_bathrooms': num_bathrooms,
            'area_sqft': area_sqft,
            'location': location,
            'age_years': age_years,
            'has_garage': has_garage,
            'total_rooms': total_rooms,
            'room_to_area_ratio': room_to_area_ratio
        }])

        prediction = model.predict(input_df)[0]
        prediction_val = max(10000.0, float(round(prediction, 2)))

        response = {
            'status': 'success',
            'predicted_price': prediction_val,
            'formatted_price': f"${prediction_val:,.2f}",
            'features': {
                'num_rooms': num_rooms,
                'num_bathrooms': num_bathrooms,
                'area_sqft': area_sqft,
                'location': location,
                'age_years': age_years,
                'has_garage': bool(has_garage)
            }
        }

        if request.is_json:
            return jsonify(response)
        return render_template('index.html', prediction_text=f"Estimated House Price: ${prediction_val:,.2f}", form_data=data)

    except Exception as e:
        if request.is_json:
            return jsonify({'status': 'error', 'message': str(e)}), 400
        return render_template('index.html', error_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
