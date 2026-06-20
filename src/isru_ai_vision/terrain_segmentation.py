import cv2
import numpy as np

class TerrainSegmentation:
    def __init__(self):
        # Mars terrain is red/orange
        self.terrain_color_range = (10, 100, 100, 30, 255, 255)  # HSV range for red
        
    def segment_terrain(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # Mask for Mars-like terrain (red/orange)
        lower_terrain = np.array([10, 100, 100])
        upper_terrain = np.array([30, 255, 255])
        terrain_mask = cv2.inRange(hsv, lower_terrain, upper_terrain)
        
        # Everything NOT terrain = obstacle
        obstacle_mask = cv2.bitwise_not(terrain_mask)
        
        return terrain_mask, obstacle_mask
