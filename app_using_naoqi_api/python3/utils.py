"""
This file contains utility functions like a dictionary to match each yoga posture with angles, instructions and images.
"""

from constants import *

poses = {
    "warrior": {
        "angles": warrior_pose_angles,
        "instructions": warrior_instructions,
        "image": "warrior.jpg",
        "initial_posture": "StandInit"
    },
    "chair": {
        "angles": chair_pose_angles,
        "instructions": chair_instructions,
        "image": "chair.jpg",
        "initial_posture": "StandInit"
    }
    # Add more poses here
}
def get_angles_for_pose(pose_name):
    return poses[pose_name]["angles"]

def get_instructions_for_pose(pose_name):
    return poses[pose_name]["instructions"]

def get_initial_posture_for_pose(pose_name):
    return poses[pose_name]["initial_posture"]