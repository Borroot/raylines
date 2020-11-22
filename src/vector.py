import math


def flipy(vector):
    return (vector[0], -vector[1])


def add(vector1, vector2):
    return tuple(sum(x) for x in zip(vector1, vector2))


def sub(vector1, vector2):
    return tuple(x - y for x, y in zip(vector1, vector2))


def mul(vector, scalar):
    return tuple(x * scalar for x in vector)


def div(vector, scalar):
    return mul(vector, 1 / scalar)


def atov(angle):  # angle to vector on unit circle
    return (math.cos(math.radians(angle)), -math.sin(math.radians(angle)))


def vtoa(vector_zero, vector):  # vector to angle on unit circle
    degr = math.degrees(math.acos(magset(flipy(sub(vector,vector_zero)),1)[0]))
    return 360 - degr if vector[1] > vector_zero[1] else degr


def magget(vector):
    return math.sqrt(sum(element ** 2 for element in vector))


def magset(vector, magnitude, curr=None):
    curr = curr if curr is not None else magget(vector)
    return tuple(map(lambda x: x / (curr / magnitude), vector))


def maglim(vector, magnitude):
    curr = magget(vector)
    return magset(vector, magnitude, curr) if curr > magnitude else vector