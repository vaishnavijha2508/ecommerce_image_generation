import cv2
import numpy as np
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def estimate_pose(image):
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    return results.pose_landmarks
