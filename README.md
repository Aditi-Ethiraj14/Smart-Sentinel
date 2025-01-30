***Shoplifting Detection System***~ ***SMART SENTINEL***

![WhatsApp Image 2025-01-26 at 15 01 46_98305f6d](https://github.com/user-attachments/assets/61251a34-60cf-45b2-971e-45efeba77ea4)

**Sneaky Moves? We See You**


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
* Numpy: For numerical operations and data manipulation.
* ML Layers: Conv2D, MaxPooling2D, Flatten, and Dense layers used in the model architecture.
* Matplotlib: Used for plotting and visualizing triggering suspicious activity over time.
* Pickle: The model is saved as a .pkl file after training, which is then loaded for real-time detection and plotting.

*Project Structure*


![image](https://github.com/user-attachments/assets/5a80847d-5410-4862-a2ce-cf6ba44d3cab)



*Prerequisites*

To run the project, make sure you have the following Python libraries installed:
scikit-learn
numpy
matplotlib
pickle

*How It Works*

* Model Training: The model is trained using scikit-learn with data from the dataset, and fine-tuned to detect shoplifting.
* Motion Detection: When a motion is detected, the trained model processes the image data to check if the activity matches the patterns of shoplifting.
* Detection & Logging as Graph: The system detects any suspicious activity detected by the model and produces a detailed graph of triggering events.
* Visualization: Using matplotlib, the suspicious activities are plotted for better understanding and further analysis.

![Screenshot 2025-01-29 183350](https://github.com/user-attachments/assets/643b4d98-6d67-439d-a951-281206f9ada4)

![image](https://github.com/user-attachments/assets/5b45da25-514d-4b83-82ee-7da360464e14)


![image](https://github.com/user-attachments/assets/b0135e3c-9ad0-4b67-856d-6f52fd6951f9)


*Graph Insights*

* Steep Lines: Sudden movements or unusual behavior (potential theft).
* Flat Regions: Minimal activity or normal customer presence.
* Patterns: Detect frequent shoplifting times or model accuracy trends.
* False Positives vs. True Positives: Evaluate detection efficiency.

*Model Workflow*

* Data Input: Test video processing.
* Feature Extraction: Analyze customer behavior.
* Suspicion Scoring & Graph Plotting: Visual representation of scores.

*Project by:- TEAM TECH ALCHEMISTS*



