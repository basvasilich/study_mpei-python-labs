import random

from Hexagon import Hexagon


def make_header() -> str:
    return f"""
N  Side  Perimeter  Area   Color
---------------------------------
"""


def make_table(hexagon_list, **keyword_parameters: str) -> str:
    result_str = make_header()
    flag = True
    for i, hexagon_item in enumerate(hexagon_list):
        if 'color' in keyword_parameters:
            if hexagon_item.color == keyword_parameters['color']:
                result_str += f"{i + 1:<3}" + hexagon_item.show()
                flag = False
        else:
            result_str += f"{i + 1:<3}" + hexagon_item.show()
    if flag and 'color' in keyword_parameters:
        return 'There no hexagon with yellow color'
    else:
        return result_str


class HexagonWithColor(Hexagon):
    def __init__(self, side):
        self.color = random.choice(['red', 'green', 'blue', 'yellow'])
        super().__init__(side)

    def show(self) -> str:
        return f"{self.side:<6.4}{self.perimeter:<11.4}{self.area:<7.4}{self.color:<6}\n"


hexagons_len = int(input('Input length of hexagons array '))
hexagons = []

for index in range(0, hexagons_len):
    hexagons.append(HexagonWithColor(float(index + 1)))
print(make_table(hexagons))
print(make_table(hexagons, color='yellow'))
