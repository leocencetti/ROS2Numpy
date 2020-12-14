# file created by Leonardo Cencetti on 12/14/20
import numpy as np
from sensor_msgs.msg import *

from ._base import ros2numpy


@ros2numpy.register(Imu)
def _(msg: Imu):
    return np.concatenate([
        ros2numpy(msg.orientation),
        ros2numpy(msg.angular_velocity),
        ros2numpy(msg.linear_acceleration),
        ros2numpy(msg.orientation_covariance),
        ros2numpy(msg.angular_velocity_covariance),
        ros2numpy(msg.linear_acceleration_covariance)
    ])
