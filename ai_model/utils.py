import cv2
import numpy as np
import os
import pyaudio
import wave

# Function to check if a path exists and create directories if not
def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to preprocess a video frame (resize, convert color, etc.)
def preprocess_frame(frame, resize_width=640):
    """Resize frame and convert to grayscale"""
    height, width = frame.shape[:2]
    aspect_ratio = width / height
    new_height = int(resize_width / aspect_ratio)
    
    resized_frame = cv2.resize(frame, (resize_width, new_height))
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    return resized_frame, gray_frame

# Function to play an audio alert (e.g., when suspicious activity is detected)
def play_audio_alert(audio_path):
    """Play an alert sound"""
    if not os.path.exists(audio_path):
        print("Audio file not found!")
        return
    
    # Open the audio file
    wf = wave.open(audio_path, 'rb')
    
    # Set up audio stream
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    
    # Read and play the audio in chunks
    data = wf.readframes(1024)
    while data:
        stream.write(data)
        data = wf.readframes(1024)
    
    # Close the audio stream
    stream.stop_stream()
    stream.close()
    p.terminate()

# Function to generate a heatmap of suspicious activity over frames (optional)
def generate_activity_heatmap(suspicious_frames, total_frames):
    """Generate a heatmap showing suspicious activity across frames"""
    heatmap = np.zeros((total_frames,))
    
    # Mark suspicious frames in the heatmap
    for frame_num in suspicious_frames:
        if frame_num < total_frames:
            heatmap[frame_num] = 1  # Mark the frame as suspicious
    
    return heatmap

# Function to save video frames with detected motion (optional)
def save_frame_with_detection(frame, output_dir, frame_number):
    """Save frames with detection to the output directory"""
    ensure_dir_exists(output_dir)
    frame_filename = os.path.join(output_dir, f"frame_{frame_number}.jpg")
    cv2.imwrite(frame_filename, frame)
    print(f"Saved frame: {frame_filename}")
    
# Example usage for the utility functions
if __name__ == "__main__":
    # Testing audio alert (ensure you have an alert audio file)
    play_audio_alert('alert_sound.wav')
    
    # Testing saving frame with motion
    cap = cv2.VideoCapture("dataset/suspicious_video.mp4")
    ret, frame = cap.read()
    if ret:
        save_frame_with_detection(frame, "output_frames", 1)
