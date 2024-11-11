"""
This file contains constants like speech that NAO says or angles of each pose that NAO performs.
"""

MAX_TIME_POSE = 10

SPEED_POSE = 0.1

INTEVAL_TIME_PHOTO = 1

IMAGE_SAVE_PATH = "/home/nao/recordings/cameras/"

JOINT_LIMITS = {
    # Available joints and their limits
    'HeadYaw': (-2.0857, 2.0857),
    'HeadPitch': (-0.6720, 0.5149),
    'LShoulderPitch': (-1.7, 1.7),
    'LShoulderRoll': (-0.3142, 1.3265),
    'LElbowYaw': (-2.0857, 2.0857),
    'LElbowRoll': (-1.5446, -0.0349),
    'LWristYaw': (-1.8238, 1.8238),
    'LHand': (0.0, 1.0),
    'LHipYawPitch': (-1.1453, 0.7408),
    'LHipRoll': (-0.3795, 0.7905),
    'LHipPitch': (-1.5359, 0.4841),
    'LKneePitch': (-0.0923, 2.1125),
    'LAnklePitch': (-1.1895, 0.9227),
    'LAnkleRoll': (-0.3979, 0.7690),
    'RShoulderPitch': (-1.7, 1.7),
    'RShoulderRoll': (-1.3265, 0.3142),
    'RElbowYaw': (-2.0857, 2.0857),
    'RElbowRoll': (0.0349, 1.5446),
    'RWristYaw': (-1.8238, 1.8238),
    'RHand': (0.0, 1.0),
    'RHipYawPitch': (-1.1453, 0.7408),
    'RHipRoll': (-0.7905, 0.3795),
    'RHipPitch': (-1.5359, 0.4841),
    'RKneePitch': (-0.1031, 2.1202),
    'RAnklePitch': (-1.1864, 0.9321),
    'RAnkleRoll': (-0.7690, 0.3979)
}

JOINTS_NAMES = [
    # Available joints
    'HeadYaw', 'HeadPitch', 'LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 
    'LElbowRoll', 'LWristYaw', 'LHand', 'LHipYawPitch', 'LHipRoll', 'LHipPitch', 
    'LKneePitch', 'LAnklePitch', 'LAnkleRoll', 'RHipYawPitch', 'RHipRoll', 
    'RHipPitch', 'RKneePitch', 'RAnklePitch', 'RAnkleRoll', 'RShoulderPitch', 
    'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand'
]

POSTURES = {
    # Available postures
    "Standing",
    "Sitting",
    "LyingBelly",
    "LyingBack",
    "LyingLeft",
    "LyingRight",
    "Belly",
    "Back",
    "Left",
    "Right",
    "UpsideDown",
    "Kneeling",
    "Lifted"
}

warrior_pose_angles = {
    'LShoulderPitch': 0, 
    'RShoulderPitch': 0, 
    'LShoulderRoll': 1.3,    # Left arm extended outward
    'RShoulderRoll': -1.3,   # Right arm extended outward
    'HeadYaw': 1.0,
    'LHipPitch': 0.127419,       # Left leg opening backward
    'RHipPitch':  0.136136,       # Right leg opening backward
    'LKneePitch': 0.584685,       # Left knee slightly bent
    'RKneePitch':  0.188496,       # Right knee slightly bent
    'RWristYaw': 0.1,
    'RElbowRoll':0.410675,
    'RElbowYaw': 1.193809,
    'RAnkleRoll':0.110789,
    'RAnklePitch': 0.410152,
    'RHipRoll': -0.376991,
    'RHipYawPitch': -1.111775,
    'LAnkleRoll': -0.110793,
    'LAnklePitch' : -0.189012,
    'LHipRoll': 0.439823,
    "LElbowRoll" : -0.410675,
    "LWristYaw":   0.100000  ,
    "LHipYawPitch" :   -1.111775 ,
    "LElbowYaw"  :-1.193809,
    'LHand': 1.0,            # Left hand open
    'RHand': 1.0             # Right hand open
    }

warrior_pose_angles2 = {
    "HeadYaw": 1.000000,
    "HeadPitch": -0.170000,
    "LShoulderPitch": -1.274173,
    "LShoulderRoll": 0.086758,
    "LElbowYaw": -1.193998,
    "LElbowRoll": -0.410205,
    "LWristYaw": 0.100000,
    "LHipYawPitch": -1.111775,
    "LHipRoll": 0.439823,
    "LHipPitch": 0.127419,
    "LKneePitch": 0.584685,
    "LAnklePitch": -0.189012,
    "LAnkleRoll": -0.110793,
    "RHipYawPitch": -1.111775,
    "RHipRoll": -0.376991,
    "RHipPitch": 0.136136,
    "RKneePitch": 0.188496,
    "RAnklePitch": 0.410152,
    "RAnkleRoll": 0.110789,
    "RShoulderPitch": -1.364130,
    "RShoulderRoll": -0.110929,
    "RElbowYaw": 1.194800,
    "RElbowRoll": 0.409233,
    "RWristYaw": 0.100000,
    "LHand": 1.000000,
    "RHand": 1.000000
}

chair_pose_angles = {
    'LShoulderPitch': -0.8,
    'RShoulderPitch': -0.8,
    'RKneePitch': 1.0,
    'LKneePitch': 1.0,
    'LHipPitch': -1.5,
    'RHipPitch': -1.5,
    'HeadPitch': -0.5,
    'LHand': 1.0,
    'RHand': 1.0
}

warrior_instructions = "Stand with your legs apart and arms extended."

chair_instructions = "Bend your knees and raise your arms."