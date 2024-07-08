#!/usr/bin/env python3
import time
import random
import numpy as np
import sys
import cv2
from formant.sdk.agent.v1 import Client as FormantClient

if __name__ == "__main__":
    print("Starting the ingestion....")
    fclient = FormantClient(
        ignore_throttled=True,
        ignore_unavailable=True
    )
    status = {"Online": True, "Button toggled": False}

    def handle_teleop(control_datapoint):
        if control_datapoint.stream == "Buttons":
            if (str(control_datapoint.bitset.bits[0]).find("true") != -1):
                status["Button toggled"] = not (status["Button toggled"])
    fclient.register_teleop_callback(handle_teleop, ["Buttons"])

    # Function to read and send video frames from a local MP4 file with adjustable frame rate
    def send_video_frame_from_file(video_path, frame_rate=20):  # Adjust frame rate as needed
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Error opening video file: {video_path}")
            return

        sleep_time = 1.0 / frame_rate  # Calculate sleep time based on desired frame rate

        while True:
            ret, frame = cap.read()  # Read frame
            if not ret:
                print("Reached end of video file")
                break  # Break loop if no more frames

            # Encode frame as JPG (adjust codec as needed)
            encoded, buffer = cv2.imencode(".jpg", frame)
            if not encoded:
                print("Error encoding image")
                continue

            fclient.post_image("usb_cam", buffer.tostring())  # Send frame to Formant

            # Handle button toggle (optional)
            if status["Button toggled"]:
                break  # Break loop if button toggled

            time.sleep(sleep_time)  # Adjust sleep time for desired frame rate

    # Rest of your code for sending other datapoints (geolocation, text, etc.)

    # Replace with the actual path to your video
    video_path = "/home/hanssel/Documents/repos/formantsdk/videoplayback.mp4"

    while True:
        send_video_frame_from_file(video_path, frame_rate=100)  # You can adjust frame rate here (e.g., send_video_frame_from_file(video_path, frame_rate=30))
