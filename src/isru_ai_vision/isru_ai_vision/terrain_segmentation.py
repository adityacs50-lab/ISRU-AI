import cv2
import numpy as np

class TerrainSegmentation:
    def __init__(self, lower_bound, upper_bound):
        """
        Initialize the terrain segmenter with HSV thresholds for obstacles.
        
        Args:
            lower_bound (list): [H, S, V] lower bound for the obstacles.
            upper_bound (list): [H, S, V] upper bound for the obstacles.
        """
        self.lower_bound = np.array(lower_bound)
        self.upper_bound = np.array(upper_bound)

    def segment(self, hsv_image):
        """
        Segments the image to find obstacle masks based on HSV thresholds.
        
        Args:
            hsv_image (np.ndarray): The HSV converted image.
            
        Returns:
            np.ndarray: Binary mask where obstacles are 255 and background is 0.
        """
        # Create a mask for dark objects (obstacles)
        obstacle_mask = cv2.inRange(hsv_image, self.lower_bound, self.upper_bound)
        
        # Terrain mask is essentially the inverse (not strictly necessary but useful)
        terrain_mask = cv2.bitwise_not(obstacle_mask)
        
        return obstacle_mask, terrain_mask
