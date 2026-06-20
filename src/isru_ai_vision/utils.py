import cv2
import numpy as np

def draw_obstacles(image, obstacles, color=(0, 255, 0)):
    """Draw obstacle markers on image"""
    for obs in obstacles:
        cv2.circle(image, obs, 10, color, -1)
    return image

def filter_obstacles_by_distance(obstacles, depth_image, min_distance=0.5):
    """Filter out obstacles too far away"""
    filtered = []
    for obs in obstacles:
        if depth_image[obs[1], obs[0]] > min_distance:
            filtered.append(obs)
    return filtered
