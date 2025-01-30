import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Function to detect movement in the video and track suspicious frames
def detect_motion(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video was loaded correctly
    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_path}")
        return []  # Return an empty list if the video couldn't be loaded

    ret, prev_frame = cap.read()

    # Check if the first frame is read correctly
    if not ret:
        print(f"Error: Unable to read the first frame of the video {video_path}")
        return []

    # Convert the first frame to grayscale
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)
    
    suspicious_frames = []  # List to store frame numbers with suspicious activity

    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_number += 1
        
        # Convert current frame to grayscale and apply Gaussian blur
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # Compute absolute difference between current frame and previous frame
        delta_frame = cv2.absdiff(prev_gray, gray)
        thresh = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        # Find contours in the thresholded image
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Loop over contours to detect motion
        motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) < 500:  # Ignore small movements
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            motion_detected = True
        
        if motion_detected:
            suspicious_frames.append(frame_number)
        
        # Display the video with highlighted movements
        cv2.imshow("Motion Detection", frame)
        prev_gray = gray
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return suspicious_frames

# Function to visualize motion detection results
def plot_motion_data(suspicious_frames, video_name):
    """Plot the number of suspicious frames detected for each video"""
    plt.figure(figsize=(10, 6))
    plt.plot(suspicious_frames, color='red', marker='o', linestyle='-', label=f"Suspicious Activity Frames ({video_name})")
    plt.xlabel('Frame Number')
    plt.ylabel('Suspicious Activity')
    plt.title(f'Motion Detection Over Time - {video_name}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    # List of video files (you can specify a folder with multiple videos)
    video_folder = r"C:\Users\Aditi Ethiraj\DESKTOP\ML Projects\Shoplifting Project\Test DataSet (User Inputs)"
    video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]

    if not video_files:
        print("No video files found in the specified folder.")
    else:
        # Prompt user to choose a video file from the list
        print("Available video files:")
        for idx, video_file in enumerate(video_files, start=1):
            print(f"{idx}. {video_file}")
        
        # Get user's choice
        choice = int(input("Enter the number of the video you want to process: "))
        
        if 1 <= choice <= len(video_files):
            selected_video = video_files[choice - 1]
            video_path = os.path.join(video_folder, selected_video)
            
            # Detect motion and get the list of suspicious frames
            suspicious_frames = detect_motion(video_path)
            
            # Visualize the suspicious frames
            plot_motion_data(suspicious_frames, selected_video)
        else:
            print("Invalid choice. Please select a valid video number.")
