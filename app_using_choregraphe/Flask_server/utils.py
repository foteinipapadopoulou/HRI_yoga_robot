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
    angle_target = np.array(angle_target)
    angle_point = np.array(angle_point)
    stage = 0
    cv2.rectangle(image, (0, 0), (370, 40), (255, 255, 255), -1)
    cv2.rectangle(image, (0, 40), (370, 370), (255, 255, 255), -1)
    cv2.putText(image, str("Score:"), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0], 2, cv2.LINE_AA)
    height, width, _ = image.shape
    message = ""
    if angle_user[0] < (angle_target[0] - 15):
        message += "Extend the right arm at elbow. "
        stage = stage + 1
        cv2.putText(image, str("Extend the right arm at elbow"), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0],
                    2, cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[0][0] * width), int(angle_point[0][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[0] > (angle_target[0] + 15):
        message += "Fold the right arm at elbow. "
        stage = stage + 1
        cv2.putText(image, str("Fold the right arm at elbow"), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0], 2,
                    cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[0][0] * width), int(angle_point[0][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[1] < (angle_target[1] - 15):
        message += "Extend the left arm at elbow. "
        stage = stage + 1
        cv2.putText(image, str("Extend the left arm at elbow"), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0],
                    2, cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[1][0] * width), int(angle_point[1][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[1] > (angle_target[1] + 15):
        message += "Fold the left arm at elbow. "
        stage = stage + 1
        cv2.putText(image, str("Fold the left arm at elbow"), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0], 2,
                    cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[1][0] * width), int(angle_point[1][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[2] < (angle_target[2] - 15):
        message += "Lift your right arm. " 
        stage = stage + 1
        cv2.putText(image, str("Lift your right arm"), (10, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0], 2,
                    cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[2][0] * width), int(angle_point[2][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[2] > (angle_target[2] + 15):
        message += "Put your arm down a little. "
        stage = stage + 1
        cv2.putText(image, str("Put your arm down a little"), (10, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0], 2,
                    cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[2][0] * width), int(angle_point[2][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[3] < (angle_target[3] - 15):
        message += "Lift your left arm. "
        stage = stage + 1
        cv2.putText(image, str("Lift your left arm"), (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0], 2,
                    cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[3][0] * width), int(angle_point[3][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[3] > (angle_target[3] + 15):
        message += "Put your arm down a little. "
        stage = stage + 1
        cv2.putText(image, str("Put your arm down a little"), (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0], 2,
                    cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[3][0] * width), int(angle_point[3][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[4] < (angle_target[4] - 15):
        message += "Extend the angle at right hip. "
        stage = stage + 1
        cv2.putText(image, str("Extend the angle at right hip"), (10, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0],
                    2, cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[4][0] * width), int(angle_point[4][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[4] > (angle_target[4] + 15):
        message += "Reduce the angle at right hip. "
        stage = stage + 1
        cv2.putText(image, str("Reduce the angle of at right hip"), (10, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    [0, 153, 0], 2, cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[4][0] * width), int(angle_point[4][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[5] < (angle_target[5] - 15):
        message += "Extend the angle at left hip. "
        stage = stage + 1
        cv2.putText(image, str("Extend the angle at left hip"), (10, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0],
                    2, cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[5][0] * width), int(angle_point[5][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[5] > (angle_target[5] + 15):
        message += "Reduce the angle at left hip. "
        stage = stage + 1
        cv2.putText(image, str("Reduce the angle at left hip"), (10, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0],
                    2, cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[5][0] * width), int(angle_point[5][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[6] < (angle_target[6] - 15):
        message += "Extend the angle of right knee. "
        stage = stage + 1
        cv2.putText(image, str("Extend the angle of right knee"), (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0],
                    2, cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[6][0] * width), int(angle_point[6][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[6] > (angle_target[6] + 15):
        message += "Reduce the angle of right knee. "
        stage = stage + 1
        cv2.putText(image, str("Reduce the angle at right knee"), (10, 320), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0],
                    2, cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[6][0] * width), int(angle_point[6][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[7] < (angle_target[7] - 15):
        message += "Extend the angle at left knee. "
        stage = stage + 1
        cv2.putText(image, str("Extend the angle at left knee"), (10, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0],
                    2, cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[7][0] * width), int(angle_point[7][1] * height)), 30, (0, 0, 255), 5)

    if angle_user[7] > (angle_target[7] + 15):
        message += "Reduce the angle at left knee. "
        stage = stage + 1
        cv2.putText(image, str("Reduce the angle at left knee"), (10, 360), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0, 153, 0],
                    2, cv2.LINE_AA)
        cv2.circle(image, (int(angle_point[7][0] * width), int(angle_point[7][1] * height)), 30, (0, 0, 255), 5)
    return message, stage

def get_pose_target_image(pose_name):
    return "images/" + poses[pose_name]["image_path"]



