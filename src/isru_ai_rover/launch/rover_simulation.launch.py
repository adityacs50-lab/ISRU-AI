import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('isru_ai_rover')
    terrain_model_path = os.path.join(pkg_share, 'models', 'terrain.sdf')
    rover_model_path = os.path.join(pkg_share, 'models', 'rover.urdf')

    return LaunchDescription([
        # Start Gazebo with terrain
        ExecuteProcess(
            cmd=['gazebo', '--verbose', terrain_model_path, '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        
        # Spawn rover in Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_rover',
            arguments=[
                '-file', rover_model_path,
                '-entity', 'rover',
                '-x', '0', '-y', '0', '-z', '1.0'
            ],
            output='screen'
        ),
        
        # Rover control node
        Node(
            package='isru_ai_rover',
            executable='rover_control.py',
            name='rover_controller',
            output='screen'
        )
    ])
