import sys
import os
import cv2
import pickle
import numpy as np
from flask import Flask, request, jsonify

# Add the ai_model directory to the system path to allow importing the feature extraction
sys.path.append(r"C:\Users\Aditi Ethiraj\DESKTOP\Hmm\ai_model")

# Import feature extraction function
from feature_extraction import extract_features  

app = Flask(__name__)

# Load the trained model
with open(r'C:\Users\Aditi Ethiraj\DESKTOP\Hmm\backend\model\suspicious_activity_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Endpoint to classify a frame
@app.route('/classify', methods=['POST'])
def classify_frame():
    try:
        # Get the frame from the request (assuming it's in base64)
        frame_data = request.files['frame'].read()  # Assuming the frame is sent as a file
        npimg = np.frombuffer(frame_data, np.uint8)
        frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        # Extract features from the frame (you can use your feature extraction logic here)
        features = extract_features(frame)

        # Predict suspicious activity
        prediction = model.predict([features])[0]

        result = 'suspicious' if prediction == 1 else 'not suspicious'
        return jsonify({'result': result}), 200

    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred while processing the frame'}), 500

if __name__ == '__main__':
    app.run(debug=True)
