import pytest


@pytest.fixture()  # decorator
def setup():
    print("Launching browser...")  # executes before every test method
    yield
    print("closing browser")  # executes after every test method
