from rmcc import MeshCode


class TestRmcc:

    def testRmccPrimary(self):
        actualStr: str = "5339"
        actual = MeshCode.parse(actualStr)
        expected = MeshCode(53, 39, -1, -1, -1, -1, -1)
        assert actual == expected
        assert actual.getDimension() == 1
        assert actual.getMeshCode() == actualStr

    def testRmccSecondary(self):
        actualStr: str = "5339-01"
        actual = MeshCode.parse(actualStr)
        expected = MeshCode(53, 39, 0, 1, -1, -1, -1)
        assert actual == expected
        assert actual.getDimension() == 2
        assert actual.getMeshCode() == actualStr

    def testRmccTertiary(self):
        actualStr: str = "5339-01-10"
        actual = MeshCode.parse(actualStr)
        expected = MeshCode(53, 39, 0, 1, 1, 0, -1)
        assert actual == expected
        assert actual.getDimension() == 3
        assert actual.getMeshCode() == actualStr

    def testRmccQuaternary(self):
        actualStr: str = "5339-01-10-1"
        actual = MeshCode.parse(actualStr)
        expected = MeshCode(53, 39, 0, 1, 1, 0, 1)
        assert actual == expected
        assert actual.getDimension() == 4
        assert actual.getMeshCode() == actualStr

    def testShiftPrimary(self):
        base: str = "5339"
        actual: MeshCode = MeshCode.parse(base)
        assert actual.getDimension() == 1
        actual.shift(1, 1)
        assert actual == MeshCode(54, 40, -1, -1, -1, -1, -1)
        actual.shift(0, 1)
        assert actual == MeshCode(54, 41, -1, -1, -1, -1, -1)
        actual.shift(-1, -1)
        assert actual == MeshCode(53, 40, -1, -1, -1, -1, -1)
        actual.shift(-1, 0)
        assert actual == MeshCode(52, 40, -1, -1, -1, -1, -1)

    def testShiftSecondary(self):
        base: str = "5339-01"
        actual: MeshCode = MeshCode.parse(base)
        assert actual.getDimension() == 2
        actual.shift(1, 1)
        assert actual == MeshCode(53, 39, 1, 2, -1, -1, -1)
        actual.shift(10, 6)
        assert actual == MeshCode(54, 40, 3, 0, -1, -1, -1)
        actual.shift(-1, -1)
        assert actual == MeshCode(54, 39, 2, 7, -1, -1, -1)
        actual.shift(-16, 0)
        assert actual == MeshCode(52, 39, 2, 7, -1, -1, -1)

    def testShiftTertiary(self):
        base: str = "5339-66-00"
        actual: MeshCode = MeshCode.parse(base)
        assert actual.getDimension() == 3
        actual.shift(1, 1)
        assert actual == MeshCode(53, 39, 6, 6, 1, 1, -1)
        actual.shift(10, 10)
        assert actual == MeshCode(53, 39, 7, 7, 1, 1, -1)
        actual.shift(10, 10)
        assert actual == MeshCode(54, 40, 0, 0, 1, 1, -1)
        actual.shift(-21, -21)
        assert actual == MeshCode(53, 39, 6, 6, 0, 0, -1)
