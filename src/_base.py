from functools import singledispatch


@singledispatch
def ros2numpy(msg):
    raise NotImplementedError

@singledispatch
def numpy2ros(msg):
    raise NotImplementedError
