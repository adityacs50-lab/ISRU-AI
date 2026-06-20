import cv2
import numpy as np
import sys
import os

# Add parent directory to path so we can import the package locally for testing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from isru_ai_vision.obstacle_detector import ObstacleDetector
from isru_ai_vision.utils import draw_obstacles

def generate_synthetic_mars_image(width=640, height=480):
    """
    Generates a synthetic image simulating Mars terrain (orange/red)
    with a few dark rocks (obstacles).
    """
    # Create an orange/red background (BGR format)
    # B: 40-60, G: 80-120, R: 180-220
    image = np.zeros((height, width, 3), dtype=np.uint8)
    image[:, :, 0] = np.random.randint(40, 60, (height, width))
    image[:, :, 1] = np.random.randint(80, 120, (height, width))
    image[:, :, 2] = np.random.randint(180, 220, (height, width))
    
    # Add a few dark rocks
    # Rock 1
    cv2.circle(image, (150, 200), 30, (20, 20, 20), -1)
    # Rock 2
    cv2.rectangle(image, (400, 300), (450, 380), (30, 30, 30), -1)
    # Rock 3 (small, might be filtered if we test min_area closely, but we'll make it big enough here)
    cv2.ellipse(image, (500, 100), (40, 20), 45, 0, 360, (10, 10, 10), -1)
    
    # Add some noise to the rocks to make them less perfect
    noise = np.random.randint(-10, 10, image.shape)
    image = np.clip(image + noise, 0, 255).astype(np.uint8)
    
    return image

def test_pipeline():
    print("Generating synthetic Mars image...")
    image = generate_synthetic_mars_image()
    
    # Save the original image for reference
    cv2.imwrite("synthetic_mars.png", image)
    
    # Use the same parameters as detector_params.yaml
    hsv_lower = [0, 0, 0]
    hsv_upper = [180, 255, 80]
    min_area = 100
    
    print("Initializing ObstacleDetector...")
    detector = ObstacleDetector(hsv_lower, hsv_upper, min_area)
    
    print("Running detection...")
    obstacles = detector.detect(image)
    
    print(f"Detected {len(obstacles)} obstacles.")
    for i, (cx, cy) in enumerate(obstacles):
        print(f"  Obstacle {i+1}: Center at ({cx}, {cy})")
        
    print("Drawing obstacles and saving to debug_output.png...")
    debug_image = draw_obstacles(image, obstacles)
    cv2.imwrite("debug_output.png", debug_image)
    print("Done. Check synthetic_mars.png and debug_output.png")

if __name__ == "__main__":
    test_pipeline()
