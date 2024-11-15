"""
This script uses MediaPipe to detect pose landmarks in an image and save them to a JSON file.
"""

import json
import os
import cv2
import math
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def save_landmarks(image_path, output_file):

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to read image {image_path}")
        return

    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if not results.pose_landmarks:
        print("No pose landmarks detected.")
        return

    landmarks = {}
    for i, landmark in enumerate(results.pose_landmarks.landmark):
        landmarks[i] = {
            "x": landmark.x,
            "y": landmark.y,
            "z": landmark.z
        }

    # Save landmarks to JSON file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(landmarks, f)
    print(f"Landmarks saved to {output_file}")

    
if __name__ == "__main__":
    # change the filename to the image you want to analyze
    filename = r"./images/warrior_pose.jpg"

    # get the name removing the extension
    name = os.path.splitext(os.path.basename(filename))[0]

    json_file = f"./landmarks/{name}.json"
    save_landmarks(filename, json_file)