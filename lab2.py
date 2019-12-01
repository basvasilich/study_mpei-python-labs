import math


def comparison_str(index_1: str, index_2: str, key: str, value: float) -> str:
    return f"{key} of hexagon {index_1} more than hexagon {index_2} by {value}"


def comparison(hexagons_list, key):
    if hexagons_list[0].__dict__[key] > hexagons_list[1].__dict__[key]:
        return comparison_str('1', '2', key, hexagons_list[0].__dict__[key] - hexagons_list[1].__dict__[key])
    elif hexagons_list[0].__dict__[key] < hexagons_list[1].__dict__[key]:
        return comparison_str('2', '1', key, hexagons_list[1].__dict__[key] - hexagons_list[0].__dict__[key])
    else:
        return f"{key} of hexagon 1 and hexagon 2 equal {hexagons_list[0].__dict__[key]}"


class Hexagon:
    def __init__(self, side: float):
        self.side = side
        self.angle = (360 / 6) * 2
        self.perimeter = 6 * side
        self.area = ((3 * math.sqrt(3)) / 2) * math.pow(side, 2)


side1 = float(input('Input side of first Hexagon '))
side2 = float(input('Input side of second Hexagon '))

hexagons = [Hexagon(side1), Hexagon(side2)]

for i, hexagon in enumerate(hexagons):
    print(f"Hexagon {i}: side = {hexagon.side}, perimeter = {hexagon.perimeter}, area = {hexagon.area}")

for key in ['perimeter', 'area', 'angle']:
    print(comparison(hexagons, key))
