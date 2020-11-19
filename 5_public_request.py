from math import tan, radians


def angle_to_grade(angle):
    """Convert angle in degree to a percentage grade"""
    return tan(radians(angle)) * 100
