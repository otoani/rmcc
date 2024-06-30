from dataclasses import dataclass


@dataclass
class MeshCode:
    primary_x: int  # lon
    primary_y: int  # lat
    secondary_x: int
    secondary_y: int
    tertiary_x: int
    tertiary_y: int
    quaternary: int

    @staticmethod
    def parse(code):
        tmp = code.split("-")

        dimension: int = len(tmp)

        primary_x: int = int(tmp[0][2:4])
        primary_y: int = int(tmp[0][0:2])
        secondary_x: int
        secondary_y: int
        tertiary_x: int
        tertiary_y: int
        quaternary: int

        if dimension >= 2:
            secondary_x = int(tmp[1][0])
            secondary_y = int(tmp[1][1])

        if dimension >= 3:
            tertiary_x = int(tmp[2][0])
            tertiary_y = int(tmp[2][1])

        if dimension >= 4:
            quaternary = int(tmp[3])

        return MeshCode(
            primary_x=primary_x,
            primary_y=primary_y,
            secondary_x=secondary_x,
            secondary_y=secondary_y,
            tertiary_x=tertiary_x,
            tertiary_y=tertiary_y,
            quaternary=quaternary,
        )

    def getDimension(self) -> int:
        if self.quaternary is not None:
            return 4
        elif self.tertiary_x is not None or self.tertiary_y is not None:
            return 3
        elif self.secondary_x is not None or self.secondary_y is not None:
            return 2
        return 1
