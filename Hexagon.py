import math


class Hexagon:
    def __init__(self, side: float):
        self.side = float(side)
        self.angle = float((360 / 6) * 2)
        self.perimeter = float(6 * side)
        self.area = float(((3 * math.sqrt(3)) / 2) * math.pow(side, 2))
