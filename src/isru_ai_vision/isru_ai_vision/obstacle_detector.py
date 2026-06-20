import cv2
import numpy as np
from .terrain_segmentation import TerrainSegmentation

class ObstacleDetector:
    def __init__(self, hsv_lower, hsv_upper, min_area=100):
        """
        Initializes the Obstacle Detector pipeline.
        
        Args:
            hsv_lower (list): Lower HSV bounds for detecting dark rocks.
            hsv_upper (list): Upper HSV bounds for detecting dark rocks.
            min_area (int): Minimum contour area to keep (filters noise).
        """
        self.segmenter = TerrainSegmentation(hsv_lower, hsv_upper)
        self.min_area = min_area

    def detect(self, image):
        """
        Main pipeline to detect obstacles in an image.
        
        Args:
            image (np.ndarray): The input BGR image.
            
        Returns:
            list of tuple: A list of (cx, cy) pixel coordinates representing obstacle centers.
        """
        # Convert BGR to HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # Segment out the terrain to find the obstacle mask
        obstacle_mask, _ = self.segmenter.segment(hsv_image)
        
        # Optional: Apply some morphological operations to remove small noise
        kernel = np.ones((5, 5), np.uint8)
        obstacle_mask = cv2.morphologyEx(obstacle_mask, cv2.MORPH_OPEN, kernel)
        
        # Find contours
        contours, _ = cv2.findContours(obstacle_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        obstacles = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area >= self.min_area:
                # Compute the center of the contour using image moments
                M = cv2.moments(cnt)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    obstacles.append((cx, cy))
                    
        return obstacles
