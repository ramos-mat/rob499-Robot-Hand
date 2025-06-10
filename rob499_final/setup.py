from setuptools import setup

package_name = 'rob499_final'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/launch_all.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your@email.com',
    description='Python ROS 2 package for robot hand gesture simulation',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'arduino_comm_node = rob499_final.arduino_comm_node:main',
            'position_input_node = rob499_final.position_input_node:main',
            'storage_manager_node = rob499_final.storage_manager_node:main',
            'averaging_node = rob499_final.averaging_node:main',
            'processed_position_node = rob499_final.processed_position_node:main',
            'keypad_trigger_node = rob499_final.keypad_trigger_node:main',
        ],
    },
)
