from rmcc import MeshCode


class TestRmcc:
    def testRmccQuaternary(self):
        actualStr: str = "5339-01-10-1"
        actual = MeshCode.parse(actualStr)
        expected = MeshCode(53, 39, 0, 1, 1, 0, 1)
        assert actual == expected
        assert actual.getDimension() == 4
        assert actual.getMeshCode() == actualStr

    def testRmccTertiary(self):
        actualStr: str = "5339-01-10"
        actual = MeshCode.parse(actualStr)
        expected = MeshCode(53, 39, 0, 1, 1, 0, -1)
        assert actual == expected
        assert actual.getDimension() == 3
        assert actual.getMeshCode() == actualStr

    def testRmccSecondary(self):
        actualStr: str = "5339-01"
        actual = MeshCode.parse(actualStr)
        expected = MeshCode(53, 39, 0, 1, -1, -1, -1)
        assert actual == expected
        assert actual.getDimension() == 2
        assert actual.getMeshCode() == actualStr

    def testRmccPrimary(self):
        actualStr: str = "5339"
        actual = MeshCode.parse(actualStr)
        expected = MeshCode(53, 39, -1, -1, -1, -1, -1)
        assert actual == expected
        assert actual.getDimension() == 1
        assert actual.getMeshCode() == actualStr
