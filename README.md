**Shoplifting Detection System**

*Overview*

This project is focused on detecting shoplifting using computer vision and machine learning techniques. We have developed a custom model for the task, trained using scikit-learn, and built the system to log and visualize suspicious activities over time.

*Key Features*

1. Machine Learning Model: Trained using scikit-learn with datasets containing instances of shoplifting. The model has been fine-tuned to detect suspicious activities accurately.
2. Computer Vision: Utilizing layers such as Conv2D, MaxPooling2D, Flatten, and Dense for efficient image processing.
3. Motion Detection: The backend is built around a motion detection system, which integrates with the trained model to detect and log suspicious activity in real time.
4. Data Logging & Visualization: Detailed logs and graphs are produced using matplotlib to visualize the detection of suspicious activities over a period of time.
5. Testing Dataset: A separate dataset containing instances of shoplifting is used to test the models performance and provide accurate detection.
   
*Technologies Used*

* Scikit-learn: Used for training the model and making predictions.
ii) Numpy: For numerical operations and data manipulation.
iii) ML Layers: Conv2D, MaxPooling2D, Flatten, and Dense layers used in the model architecture.
iv) Matplotlib: Used for plotting and visualizing triggering suspicious activity over time.
v) Pickle: The model is saved as a .pkl file after training, which is then loaded for real-time detection and plotting.

*Project Structure*
![image](https://github.com/user-attachments/assets/5a80847d-5410-4862-a2ce-cf6ba44d3cab)


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
