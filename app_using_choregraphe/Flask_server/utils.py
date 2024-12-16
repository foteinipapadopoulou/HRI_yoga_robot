import numpy as np
import cv2
import math
from scipy import spatial

from constants import poses


def calculate_angle(a, b, c):
    """
    Calculate the angle between three points
    """
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

def display_angles(image, points, angles):
    for idx, (point, angle) in enumerate(zip(points, angles), start=1):
        cv2.putText(image, str(idx), tuple(np.multiply(point, image.shape[1::-1]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(image, str(int(angle)), (10, 40 * idx), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 153, 0), 2, cv2.LINE_AA)
        
def Average(lst):
    return sum(lst) / len(lst)

def diff_compare_angle(x,y):
    new_x = []
    for i,j in zip(range(len(x)),range(len(y))):
        z = np.abs(x[i] - y[j])/((x[i]+ y[j])/2)
        new_x.append(z)
    return Average(new_x)

def dif_compare(x,y):
    average = []
    for i,j in zip(range(len(list(x))),range(len(list(y)))):
        result = 1 - spatial.distance.cosine(list(x[i].values()),list(y[j].values()))
        average.append(result)
    score = math.sqrt(2*(1-round(Average(average),2)))
    #print(Average(average))
    return score

def compare_pose(image, angle_point, angle_user, angle_target):
    angle_user = np.array(angle_user)
    print(angle_user)
    angle_target = np.array(angle_target)
    angle_point = np.array(angle_point)
    stage = 0
    cv2.rectangle(image, (0, 0), (370, 40), (255, 255, 255), -1)
    cv2.rectangle(image, (0, 40), (370, 370), (255, 255, 255), -1)
    cv2.putText(image, str("Score:"), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0], 2, cv2.LINE_AA)
    height, width, _ = image.shape
    
    feedback = []
    tolerance = 20
    
    # In order of overall importance in alignment, balance and injury
    checks = [
        ("left elbow", "Extend the left arm at elbow.", "Fold the left arm at elbow."),
        ("right elbow", "Extend the right arm at elbow.", "Fold the right arm at elbow."),
        ("left shoulder", "Lift your left arm.", "Put your left arm down a little."),
        ("right shoulder", "Lift your right arm.", "Put your right arm down a little."),
        ("left hip", "Extend the angle at left hip.", "Reduce the angle at left hip."),
        ("right hip", "Extend the angle at right hip.", "Reduce the angle at right hip."),
        ("left knee", "Extend the angle of left knee.", "Reduce the angle of left knee."),
        ("right knee", "Extend the angle at right knee.", "Reduce the angle at right knee.")
    ]
    
    for i, (joint_name, msg_increase, msg_decrease) in enumerate(checks):
        if len(feedback) >= 2: # I chose to limit the feedback to 2 to reduce cognitive load and keep the rythm.
            break
        if angle_user[i] < (angle_target[i] - tolerance):
            feedback.append(msg_increase)
            cv2.putText(image, msg_increase, (10, 60 + 20 * len(feedback)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0], 2, cv2.LINE_AA)
            cv2.circle(image, (int(angle_point[i][0] * width), int(angle_point[i][1] * height)), 30, (0, 0, 255), 5)
        elif angle_user[i] > (angle_target[i] + tolerance):
            feedback.append(msg_decrease)
            cv2.putText(image, msg_decrease, (10, 60 + 20 * len(feedback)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0], 2, cv2.LINE_AA)
            cv2.circle(image, (int(angle_point[i][0] * width), int(angle_point[i][1] * height)), 30, (0, 0, 255), 5)

    return " ".join(feedback), len(feedback)

def get_pose_target_image(pose_name):
    return "images/" + poses[pose_name]["image_path"]



