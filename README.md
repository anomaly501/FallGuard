# YOLOv8 Fall Detection Project

This project utilizes a custom-trained YOLOv8 model to detect falls in both pre-recorded video files and live webcam streams. It uses the Ultralytics library for detection and OpenCV for video handling.

## Features

*   **Video File Detection:** Processes a video file, performs fall detection frame-by-frame, and saves the output as a new video with bounding boxes overlaid.
*   **Real-time Webcam Detection:** Captures video from a webcam, performs real-time fall detection, and displays the annotated stream.
*   **Configurable Confidence:** Allows setting a confidence threshold to filter out low-confidence detections.

## Requirements

*   Python 3.8+
*   Ultralytics YOLOv8: `pip install ultralytics`
*   OpenCV for Python: `pip install opencv-python`
*   A custom-trained YOLOv8 model file).

## Installation

1.  **Clone the repository (or download the scripts):**
    ```bash
    # If you have a git repository
    # git clone <your-repo-url>
    # cd <your-repo-directory>
    ```
    Alternatively, save the first Python script provided as `detect_video.py` and the second as `detect_webcam.py`.

2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m  ProjectV  ProjectV
    # On Windows
    .\ ProjectV\Scripts\activate
    # On macOS/Linux
    source  ProjectV/bin/activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install ultralytics opencv-python
    ```

4.  **Place your trained model:**
    Ensure you have your trained `best.pt` file (or whichever model file you are using). You will need to update the `model_path` variable in both scripts to point to its exact location.

## Configuration

Before running the scripts, you might need to adjust the following variables within the Python files:

**In both `detect_video.py` and `detect_webcam.py`:**

*   `model_path`: **Crucial!** Update this to the absolute or relative path of your trained `.pt` model file. The current examples use absolute paths like `D:\FallGuard\...` and `D:\fall detection\...`.
*   `confidence_threshold`: Adjust the minimum confidence score (0.0 to 1.0) for detections to be considered valid. Default is `0.7`.

**In `detect_video.py`:**

*   `input_video_path`: Path to the video file you want to process.
*   `output_video_path`: Path where the processed video with detections will be saved.

**In `detect_webcam.py`:**

*   `cv2.VideoCapture(1)`: The index `1` refers to the webcam device. If you only have one webcam, this might need to be `0`. If you have multiple, you might need to experiment to find the correct index.

## Usage

### 1. Detecting Falls in a Video File

1.  Ensure you have saved the first script as `detect_video.py`.
2.  Modify the `model_path`, `input_video_path`, and `output_video_path` variables inside `detect_video.py` to match your setup.
3.  Run the script from your terminal:
    ```bash
    python detect_video.py
    ```
4.  The script will process the input video frame by frame.
5.  An OpenCV window titled 'YOLOv8 Real-Time Detection' will pop up, showing the processed frames.
6.  Press 'q' to stop the processing early.
7.  Once completed or stopped, the annotated video will be saved to the specified `output_video_path`. A confirmation message will be printed.

### 2. Detecting Falls from a Webcam

1.  Ensure you have saved the second script as `detect_webcam.py`.
2.  Modify the `model_path` variable inside `detect_webcam.py`.
3.  Adjust the webcam index in `cv2.VideoCapture(index)` if necessary (e.g., change `1` to `0`).
4.  Run the script from your terminal:
    ```bash
    python detect_webcam.py
    ```
5.  An OpenCV window titled 'YOLOv8 Real-Time Detection' will appear, displaying the live webcam feed with bounding boxes around detected falls.
6.  Press 'q' while the OpenCV window is active to stop the webcam feed and exit the script.

## Notes

*   The performance (frames per second) will depend heavily on your hardware (CPU, GPU) and the resolution of the video/webcam feed.
*   Ensure the paths in the scripts use the correct separators for your operating system (e.g., `\` for Windows, `/` for Linux/macOS) or use `os.path.join` for better portability. The provided examples use Windows-style paths.

## Acknowledgments

*   This project relies heavily on the [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) library.
*   Uses [OpenCV](https://opencv.org/) for video input/output and display.
