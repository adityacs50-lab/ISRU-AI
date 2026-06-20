import cv2
import numpy as np

def draw_obstacles(image, obstacles):
    """
    Draws markers on the detected obstacles on the given image.
    
    Args:
        image (np.ndarray): The BGR image to draw on.
        obstacles (list of tuple): List of (cx, cy) pixel coordinates.
        
    Returns:
        np.ndarray: Image with obstacle centers drawn.
    """
    debug_image = image.copy()
    for (cx, cy) in obstacles:
        # Draw a red circle at the center
        cv2.circle(debug_image, (cx, cy), 5, (0, 0, 255), -1)
        # Add some text
        cv2.putText(debug_image, f"({cx}, {cy})", (cx + 10, cy),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    return debug_image

def filter_obstacles_by_distance(obstacles, depth_image, min_distance=0.0):
    """
    Optional utility to filter obstacles if a depth image is provided.
    Placeholder for future integration with depth cameras.
    """
    valid_obstacles = []
    # Implementation depends on depth map format
    return obstacles
