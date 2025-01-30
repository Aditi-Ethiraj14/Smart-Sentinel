**Shoplifting Detection System**

*Overview*/n

This project is focused on detecting shoplifting using computer vision and machine learning techniques. We have developed a custom model for the task, trained using scikit-learn, and built the system to log and visualize suspicious activities over time./n

*Key Features*

1. Machine Learning Model: Trained using scikit-learn with datasets containing instances of shoplifting. The model has been fine-tuned to detect suspicious activities accurately./n
2. Computer Vision: Utilizing layers such as Conv2D, MaxPooling2D, Flatten, and Dense for efficient image processing.
Motion Detection: The backend is built around a motion detection system, which integrates with the trained model to detect and log suspicious activity in real time.
Data Logging & Visualization: Detailed logs and graphs are produced using matplotlib to visualize the detection of suspicious activities over a period of time.
Testing Dataset: A separate dataset containing instances of shoplifting is used to test the models performance and provide accurate detection.
Technologies Used
Scikit-learn: Used for training the model and making predictions.
Numpy: For numerical operations and data manipulation.
TensorFlow/Keras Layers: Conv2D, MaxPooling2D, Flatten, and Dense layers used in the model architecture.
Matplotlib: Used for plotting and visualizing triggering suspicious activity over time.
Pickle: The model is saved as a .pkl file after training, which is then loaded for real-time detection and logging.
Project Structure
motion_detection.py: Contains the motion detection logic, essential for detecting suspicious behavior.
feature_extraction.py: Extracts features from the video footage for model training.
model_training.py: Defines the model and trains it using the imported dataset.
model.pkl: The trained machine learning model saved as a pickle file.
testing_dataset/: A separate folder containing instances of shoplifting used for testing the model.
logs/: Logs and graphs generated during the testing phase, showing detection of suspicious activities over time.
How It Works
Model Training: The model is trained using scikit-learn with data from the dataset, and fine-tuned to detect shoplifting.
Motion Detection: When a motion is detected, the trained model processes the image data to check if the activity matches the patterns of shoplifting.
Detection & Logging: The system logs any suspicious activity detected by the model and produces a detailed graph of triggering events.
Visualization: Using matplotlib, the suspicious activities are plotted for better understanding and further analysis.
Getting Started
Prerequisites
To run the project, make sure you have the following Python libraries installed:

scikit-learn
numpy
matplotlib
tensorflow (for Conv2D, MaxPooling2D, etc.)
pickle
Install them using pip:

bash
Copy
Edit
