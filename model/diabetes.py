import joblib
import numpy as np

def load_diabetes_model():
    # Load the machine learning model
    model = joblib.load('model/diabetes_model.pkl')  # Adjust the filename accordingly
    return model

def predict_diabetes(features, model):
    # Ensure that the features are in the same order as in your training data
    features_array = np.array(features).reshape(1, -1)
    
    # Make a prediction
    prediction = model.predict(features_array)[0]

    return prediction
