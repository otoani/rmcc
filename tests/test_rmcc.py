from rmcc import MeshCode
from rmcc.exception import InvalidElementError
import pytest


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
        actualStr: str = "5339-01-10-4"
        actual = MeshCode.parse(actualStr)
        expected = MeshCode(53, 39, 0, 1, 1, 0, 4)
        assert actual == expected
        assert actual.getDimension() == 4
        assert actual.getMeshCode() == actualStr

    def testInvalidMeshCode(self):
        with pytest.raises(InvalidElementError) as e:
            MeshCode(-1, 1, 1, 1, 1, 1, 1)
        assert str(e.value) == "y=-1, x=1 is invalid element."
        with pytest.raises(InvalidElementError) as e:
            MeshCode(1, -1, 1, 1, 1, 1, 1)
        assert str(e.value) == "y=1, x=-1 is invalid element."

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

    def testShiftQuaternary(self):
        base: str = "5339-66-00-1"
        actual: MeshCode = MeshCode.parse(base)
        assert actual.getDimension() == 4
        actual.shift(1, 1)
        assert actual == MeshCode(53, 39, 6, 6, 0, 0, 4)
        actual.shift(20, 20)
        assert actual == MeshCode(53, 39, 7, 7, 0, 0, 4)
        actual.shift(10, 10)
        assert actual == MeshCode(53, 39, 7, 7, 5, 5, 4)
        actual.shift(-21, -20)
        assert actual == MeshCode(53, 39, 6, 6, 5, 5, 2)

    def testCalNeighbors1(self):
        base: str = "5339-00-00-1"
        baseMeshCode: MeshCode = MeshCode.parse(base)
        actual = baseMeshCode.calNeighbors(1)
        # [
        #     [-1,-1], [-1,0], [-1,1],
        #     [0,-1], [0,0], [0,1],
        #     [1,-1], [1,0], [1,1]
        # ]
        assert len(actual) == 9
        assert actual[0] == MeshCode.parse("5238-77-99-4")
        assert actual[1] == MeshCode.parse("5338-07-09-2")
        assert actual[2] == MeshCode.parse("5338-07-09-4")
        assert actual[3] == MeshCode.parse("5239-70-90-3")
        assert actual[4] == MeshCode.parse(base)
        assert actual[5] == MeshCode.parse("5339-00-00-3")
        assert actual[6] == MeshCode.parse("5239-70-90-4")
        assert actual[7] == MeshCode.parse("5339-00-00-2")
        assert actual[8] == MeshCode.parse("5339-00-00-4")

    def testCalNeighbors2(self):
        base: str = "5339-00-00-1"
        baseMeshCode: MeshCode = MeshCode.parse(base)
        actual = baseMeshCode.calNeighbors(2)
        # [
        #     [-2,-2],[-2,-1],[-2,0],[-2,1],[-2,2],
        #     [-1,-2],[-1,-1],[-1,0],[-1,1],[-1,2],
        #     [0,-2],[0,-1],[0,0],[0,1],[0,2],
        #     [1,-2],[1,-1],[1,0],[1,1],[1,2],
        #     [2,-2],[2,-1],[2,0],[2,1],[2,2],
        # ]
        assert len(actual) == 25

        assert actual[0] == MeshCode.parse("5238-77-99-1")
        assert actual[1] == MeshCode.parse("5238-77-99-3")
        assert actual[2] == MeshCode.parse("5338-07-09-1")
        assert actual[3] == MeshCode.parse("5338-07-09-3")
        assert actual[4] == MeshCode.parse("5338-07-19-1")
        assert actual[5] == MeshCode.parse("5238-77-99-2")
        assert actual[6] == MeshCode.parse("5238-77-99-4")
        assert actual[7] == MeshCode.parse("5338-07-09-2")
        assert actual[8] == MeshCode.parse("5338-07-09-4")
        assert actual[9] == MeshCode.parse("5338-07-19-2")
        assert actual[10] == MeshCode.parse("5239-70-90-1")
        assert actual[11] == MeshCode.parse("5239-70-90-3")
        assert actual[12] == MeshCode.parse(base)
        assert actual[13] == MeshCode.parse("5339-00-00-3")
        assert actual[14] == MeshCode.parse("5339-00-10-1")
        assert actual[15] == MeshCode.parse("5239-70-90-2")
        assert actual[16] == MeshCode.parse("5239-70-90-4")
        assert actual[17] == MeshCode.parse("5339-00-00-2")
        assert actual[18] == MeshCode.parse("5339-00-00-4")
        assert actual[19] == MeshCode.parse("5339-00-10-2")
        assert actual[20] == MeshCode.parse("5239-70-91-1")
        assert actual[21] == MeshCode.parse("5239-70-91-3")
        assert actual[22] == MeshCode.parse("5339-00-01-1")
        assert actual[23] == MeshCode.parse("5339-00-01-3")
        assert actual[24] == MeshCode.parse("5339-00-11-1")
