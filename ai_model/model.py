# ai_model/model.py

import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import numpy as np
import cv2
import os

def preprocess_frame(frame, target_size=(224, 224)):
    """Preprocess frames by resizing and normalizing"""
    frame_resized = cv2.resize(frame, target_size)
    return frame_resized.astype("float32") / 255.0

def build_model(input_shape=(224, 224, 3)):
    """Build the CNN model"""
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))  # Binary classification (normal/suspicious)
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    return model

def load_data(data_dir):
    """Load and preprocess video frames"""
    X, y = [], []
    for label in ['normal', 'suspicious']:
        video_folder = os.path.join(data_dir, label)
        for video_name in os.listdir(video_folder):
            video_path = os.path.join(video_folder, video_name)
            cap = cv2.VideoCapture(video_path)
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame_normalized = preprocess_frame(frame)
                X.append(frame_normalized)
                y.append(0 if label == 'normal' else 1)
            cap.release()
    return np.array(X), np.array(y)

# Example usage for training
if __name__ == "__main__":
    data_dir = "C:\Users\Aditi Ethiraj\DESKTOP\ML Projects\Shoplifting Project\dataset"  # Dataset with normal and suspicious video folders
    X_train, y_train = load_data(data_dir)
    
    model = build_model()
    model.fit(X_train, y_train, epochs=10, batch_size=32)
    model.save("shoplifting_model.h5")  # Save the trained model
