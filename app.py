from flask import Flask, render_template, request, jsonify
from diabetes import load_diabetes_model, predict_diabetes

app = Flask(__name__)

# Load the machine learning model
model = load_diabetes_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request
    data = request.get_json()

    # Extract features from input data
    preg = float(data['preg'])
    plas = float(data['plas'])
    pres = float(data['pres'])
    skin = float(data['skin'])
    test = float(data['test'])
    mass = float(data['mass'])
    pedi = float(data['pedi'])
    age = float(data['age'])

    # Make a prediction
    features = [preg, plas, pres, skin, test, mass, pedi, age]
    prediction = predict_diabetes(features, model)

    # Return the prediction as JSON
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)