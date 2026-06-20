import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'isru_ai_vision'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('isru_ai_vision/config/*.yaml')),
    ],
    install_requires=['setuptools', 'opencv-python', 'numpy'],
    zip_safe=True,
    maintainer='ISRU AI',
    maintainer_email='contact@isruai.example.com',
    description='Obstacle detection and terrain segmentation for ISRU AI rover',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vision_node = isru_ai_vision.vision_node:main'
        ],
    },
)
