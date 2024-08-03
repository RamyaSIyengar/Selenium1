import pytest


class TestClass:

    @pytest.mark.run(order=3)
    def test_method_c(self):
        print("Running Method C")

    @pytest.mark.run(order=1)
    def test_method_a(self):
        print("Running Method A")

    @pytest.mark.run(order=5)
    def test_method_f(self):
        print("Running Method F")

    @pytest.mark.run(order=4)
    def test_method_d(self):
        print("Running Method D")

    @pytest.mark.run(order=2)
    def test_method_b(self):
        print("Running Method B")

# instead of using customized markers, you can use default marker => run to get the job done
# mention order no inside run [@pytest.mark.run(order=1)] 1, 2, 3 in which order you want to run tests
