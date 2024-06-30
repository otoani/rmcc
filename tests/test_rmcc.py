from rmcc import MeshCode


class TestRmcc:
    def test_Rmcc(self):
        actual = MeshCode.parse("5339-00-00-1")
        print(actual)
        expected = MeshCode(39, 53, 0, 0, 0, 0, 1)
        assert actual == expected
        # self.assertEqual(actual.getDimension, 4)


# if __name__ == "__main__":
#     unittest.main()
