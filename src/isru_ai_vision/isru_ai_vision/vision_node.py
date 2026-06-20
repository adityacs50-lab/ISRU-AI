import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped
from cv_bridge import CvBridge
import cv2
import yaml
import os
from ament_index_python.packages import get_package_share_directory

from .obstacle_detector import ObstacleDetector
from .utils import draw_obstacles

class VisionNode(Node):
    def __init__(self):
        super().__init__('vision_node')
        self.get_logger().info("Initializing ISRU AI Vision Node...")
        
        # Load parameters
        config_path = os.path.join(
            get_package_share_directory('isru_ai_vision'),
            'config',
            'detector_params.yaml'
        )
        
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            
        hsv_lower = config['obstacle_detection']['hsv']['lower_bound']
        hsv_upper = config['obstacle_detection']['hsv']['upper_bound']
        min_area = config['obstacle_detection']['contours']['min_area']
        
        # Initialize detector
        self.detector = ObstacleDetector(hsv_lower, hsv_upper, min_area)
        self.bridge = CvBridge()
        
        # Publishers and Subscribers
        self.image_sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )
        
        # We publish the obstacles as PointStamped (one per obstacle for simplicity)
        # Alternatively, a custom message array could be used.
        self.obstacle_pub = self.create_publisher(PointStamped, '/obstacles', 10)
        
        self.get_logger().info("Vision Node is ready and listening to /camera/image_raw.")

    def image_callback(self, msg):
        try:
            # Convert ROS Image to OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f"Failed to convert image: {e}")
            return
            
        # Detect obstacles
        obstacles = self.detector.detect(cv_image)
        
        # Publish each obstacle
        for (cx, cy) in obstacles:
            pt_msg = PointStamped()
            pt_msg.header.stamp = self.get_clock().now().to_msg()
            pt_msg.header.frame_id = msg.header.frame_id # Same frame as camera
            pt_msg.point.x = float(cx)
            pt_msg.point.y = float(cy)
            pt_msg.point.z = 0.0 # Pixel coordinates, z is 0
            self.obstacle_pub.publish(pt_msg)
            
        # Optionally, log how many were found
        if len(obstacles) > 0:
            self.get_logger().debug(f"Detected {len(obstacles)} obstacles.")

def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()
