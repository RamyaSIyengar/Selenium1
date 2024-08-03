import pytest


class TestClass:

    @pytest.mark.third
    def test_method_c(self):
        print("Running Method C")

    @pytest.mark.first
    def test_method_a(self):
        print("Running Method A")

    @pytest.mark.fifth
    def test_method_f(self):
        print("Running Method F")

    @pytest.mark.fourth
    def test_method_d(self):
        print("Running Method D")

    @pytest.mark.second
    def test_method_b(self):
        print("Running Method B")


# install pytest-ordering package to make this work
# the decorator @pytest.mark. then you will provide the custom name for each method
# and then you will create pytest.ini file to specify which method will come first

# pytest.ini  => contains customized markers
#  [pytest]
#
# markers =
#     A
#     B
#     C
#     D
#     F


