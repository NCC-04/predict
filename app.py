from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained model
model_path = 'model.pickle'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    sqft = int(request.form['Squareft'])
    bhk = int(request.form['uiBHK'])
    bath = int(request.form['uiBathrooms'])
    location = request.form['uiLocation']

    # Prepare features for model (update this as per your model's requirements)
    # Example: If your model uses one-hot encoding for location, handle it here.
    # For demonstration, let's assume model expects [sqft, bhk, bath, location_index]
    # You need to map location to an index or one-hot vector as per your model.
    # Example mapping:
    location_map = {
        "Kothanur": 0,
        "NGR Layout": 1,
        "Poorna Pragna Layout": 2,
        "HBR Layout": 3
    }
    location_index = location_map.get(location, 0)

    features = np.array([[sqft, bhk, bath, location_index]])
    prediction = model.predict(features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'Estimated Price: ₹ {output} Lakhs')

if __name__ == "__main__":
    app.run(debug=True)