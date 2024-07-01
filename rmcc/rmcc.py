from dataclasses import dataclass

from rmcc.exception import UnimplementedError


@dataclass
class MeshCode:
    primary_y: int  # lat
    primary_x: int  # lon
    secondary_y: int
    secondary_x: int
    tertiary_y: int
    tertiary_x: int
    quaternary: int

    @staticmethod
    def parse(code):
        tmp = code.split("-")

        dimension: int = len(tmp)

        primary_y: int = int(tmp[0][0:2])
        primary_x: int = int(tmp[0][2:4])
        secondary_y: int = int(tmp[1][0]) if dimension >= 2 else -1
        secondary_x: int = int(tmp[1][1]) if dimension >= 2 else -1
        tertiary_y: int = int(tmp[2][0]) if dimension >= 3 else -1
        tertiary_x: int = int(tmp[2][1]) if dimension >= 3 else -1
        quaternary: int = int(tmp[3]) if dimension >= 4 else -1

        return MeshCode(
            primary_y=primary_y,
            primary_x=primary_x,
            secondary_y=secondary_y,
            secondary_x=secondary_x,
            tertiary_y=tertiary_y,
            tertiary_x=tertiary_x,
            quaternary=quaternary,
        )

    def getDimension(self) -> int:
        if self.quaternary >= 0:
            return 4
        if self.tertiary_x >= 0 or self.tertiary_y >= 0:
            return 3
        if self.secondary_x >= 0 or self.secondary_y >= 0:
            return 2
        return 1

    def getMeshCode(self) -> str:
        if self.quaternary >= 0:
            return "{}{}-{}{}-{}{}-{}".format(
                self.primary_y,
                self.primary_x,
                self.secondary_y,
                self.secondary_x,
                self.tertiary_y,
                self.tertiary_x,
                self.quaternary,
            )
        if self.tertiary_x >= 0 or self.tertiary_y >= 0:
            return "{}{}-{}{}-{}{}".format(
                self.primary_y,
                self.primary_x,
                self.secondary_y,
                self.secondary_x,
                self.tertiary_y,
                self.tertiary_x,
            )
        if self.secondary_x >= 0 or self.secondary_y >= 0:
            return "{}{}-{}{}".format(
                self.primary_y,
                self.primary_x,
                self.secondary_y,
                self.secondary_x,
            )
        return "{}{}".format(self.primary_y, self.primary_x)

    def shiftPrimary(self, dy, dx):
        self.primary_y += dy
        self.primary_x += dx

        return

    def shiftSecondary(self, dy, dx):
        self.secondary_y += dy
        self.secondary_x += dx

        qy, ry = self.secondary_y // 8, self.secondary_y % 8
        qx, rx = self.secondary_x // 8, self.secondary_x % 8

        self.shiftPrimary(qy, qx)
        self.secondary_y, self.secondary_x = ry, rx

        return

    def shiftTertiary(self, dy, dx):
        self.tertiary_y += dy
        self.tertiary_x += dx

        qy, ry = self.tertiary_y // 10, self.tertiary_y % 10
        qx, rx = self.tertiary_x // 10, self.tertiary_x % 10

        self.shiftSecondary(qy, qx)
        self.tertiary_y, self.tertiary_x = ry, rx

        return

    def shift(self, dy, dx):
        if self.getDimension() == 4:
            raise UnimplementedError(str(self.getDimension()))
        if self.getDimension == 3:
            self.shiftTertiary(dy, dx)
            return
        if self.getDimension == 2:
            self.shiftSecondary(dy, dx)
            return
        self.shiftPrimary(dy, dx)
        return
