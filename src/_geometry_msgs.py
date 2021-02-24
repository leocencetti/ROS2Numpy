# file created by Leonardo Cencetti on 12/14/20

import numpy as np
from geometry_msgs.msg import *

from ._base import ros2numpy


@ros2numpy.register(Quaternion)
def _(msg: Quaternion):
    return np.array([
        msg.x,
        msg.y,
        msg.z,
        msg.w
    ])


@ros2numpy.register(Vector3)
@ros2numpy.register(Point)
@ros2numpy.register(Point32)
def _(msg):
    return np.array([
        msg.x,
        msg.y,
        msg.z
    ])


@ros2numpy.register(Accel)
def _(msg: Accel):
    return np.concatenate([
        ros2numpy(msg.linear),
        ros2numpy(msg.angular)
    ])


@ros2numpy.register(Pose)
def _(msg: Pose):
    return np.concatenate([
        ros2numpy(msg.position),
        ros2numpy(msg.orientation)
    ])


@ros2numpy.register(Pose2D)
def _(msg: Pose2D):
    return np.array([
        msg.x,
        msg.y,
        msg.theta
    ])

@ros2numpy.register(TwistStamped)
def _(msg: TwistStamped):
    return np.concatenate([
        ros2numpy(msg.twist)
    ])

@ros2numpy.register(Twist)
def _(msg: Twist):
    return np.concatenate([
        ros2numpy(msg.linear),
        ros2numpy(msg.angular)
    ])