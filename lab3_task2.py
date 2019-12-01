from Hexagon import Hexagon


def make_header() -> str:
    return f"""
N  Side  Perimeter  Area
-------------------------
"""


def make_table(hexagon_list) -> str:
    result_str = make_header()
    for i, hexagon_item in enumerate(hexagon_list):
        result_str += f"{i + 1:<3}" + hexagon_item.show()
    return result_str


class HexagonWithShow(Hexagon):
    def show(self) -> str:
        return f"{self.side:<6.4}{self.perimeter:<11.4}{self.area:<6.4}\n"


hexagons_len = int(input('Input length of hexagons array '))
hexagons = []

for index in range(0, hexagons_len):
    hexagons.append(HexagonWithShow(float(index + 1)))

f = open('output.txt', 'w')
f.write(make_table(hexagons))

hexagons[2].__init__(float(input("Input side of third instance ")))

print(make_table(hexagons))
