from cyberlib_base.arithmetic import add2


def add3(x: int, y: int, z: int) -> int:
    return add2(add2(x, y), z)
