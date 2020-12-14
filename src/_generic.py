import numpy as np

from ._base import ros2numpy


@ros2numpy.register(tuple)
@ros2numpy.register(list)
def _(msg):
    return np.fromiter(msg, dtype=float)
