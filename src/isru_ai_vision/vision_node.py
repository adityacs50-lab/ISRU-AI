import rclpy
from obstacle_detector import ObstacleDetector

def main():
    rclpy.init()
    detector = ObstacleDetector()
    rclpy.spin(detector)
    detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
