const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const statusText = document.getElementById("status");

// Access the webcam and display the video on the page
navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
        video.srcObject = stream;
    })
    .catch((err) => console.error("Error accessing camera:", err));

// Function to send video frame to Flask backend for classification
function sendFrame() {
    const ctx = canvas.getContext("2d");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    // Draw the current video frame onto the canvas
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Convert the canvas image to a Blob object
    canvas.toBlob((blob) => {
        const formData = new FormData();
        formData.append("frame", blob);

        // Send the frame to the backend for classification
        fetch("http://127.0.0.1:5000/classify", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Display the result of the classification
            if (data.result === 'suspicious') {
                statusText.innerText = "Shoplifting Detected!";
            } else {
                statusText.innerText = "No Suspicious Activity";
            }
        })
        .catch(error => console.error("Error:", error));
    }, "image/jpeg");
}

// Send a frame every 2 seconds
setInterval(sendFrame, 2000);
