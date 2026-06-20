import cv2
import numpy as np
import sys

try:
    from rclpy.node import Node
    from sensor_msgs.msg import Image
    from geometry_msgs.msg import PointStamped
    import rclpy
except ImportError:
    # Mock classes for testing without ROS 2 environment
    class Node:
        def __init__(self, name):
            pass
        def create_subscription(self, *args, **kwargs):
            return None
        def create_publisher(self, *args, **kwargs):
            return None
    class Image:
        pass
    class PointStamped:
        class Header:
            stamp = None
        class Point:
            x = 0.0
            y = 0.0
        header = Header()
        point = Point()

class ObstacleDetector(Node):
    def __init__(self):
        super().__init__('obstacle_detector')
        
        # Subscribers
        self.image_sub = self.create_subscription(Image, '/camera/image', 10)
        
        # Publishers
        self.obstacle_pub = self.create_publisher(PointStamped, '/obstacles', 10)
        
        # Detection parameters
        self.obstacle_color_threshold = (100, 50, 50)  # Rock color (darker than terrain)
        self.min_obstacle_size = 50  # Minimum pixels to be an obstacle
        
    def image_callback(self, msg):
        # Convert ROS Image to OpenCV format
        image = self.convert_ros_to_opencv(msg)
        
        # Detect obstacles
        obstacles = self.detect_obstacles(image)
        
        # Publish obstacle coordinates
        for obs in obstacles:
            self.publish_obstacle(obs)
    
    def convert_ros_to_opencv(self, ros_image):
        # Convert ROS Image message to numpy array
        import cv2
        from cv_bridge import CvBridge
        bridge = CvBridge()
        return bridge.imgmsg_to_cv2(ros_image, desired_encoding='bgr8')
    
    def detect_obstacles(self, image):
        # Convert to HSV color space
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # Threshold for rock obstacles (darker colors)
        lower_rock = np.array([0, 0, 10])
        upper_rock = np.array([180, 255, 50])
        mask = cv2.inRange(hsv, lower_rock, upper_rock)
        
        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Filter contours by size
        obstacles = []
        for contour in contours:
            if cv2.contourArea(contour) > self.min_obstacle_size:
                # Get center point
                M = cv2.moments(contour)
                if M['m00'] != 0:
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    obstacles.append((cx, cy))
        
        return obstacles
    
    def publish_obstacle(self, obstacle):
        # Publish obstacle coordinates to ROS 2
        point = PointStamped()
        # Mocking time for standalone testing without rclpy
        if 'rclpy' in sys.modules:
            point.header.stamp = self.get_clock().now().to_msg()
        point.point.x = float(obstacle[0])
        point.point.y = float(obstacle[1])
        self.obstacle_pub.publish(point)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, help='Path to test image')
    args = parser.parse_args()
    
    if args.image:
        image = cv2.imread(args.image)
        if image is not None:
            detector = ObstacleDetector()
            obstacles = detector.detect_obstacles(image)
            print("Detected obstacles at:")
            for obs in obstacles:
                print(obs)
        else:
            print("Could not read image:", args.image)
