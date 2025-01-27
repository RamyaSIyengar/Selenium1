import pytest


@pytest.fixture
def input_value():
    input_value = 39
    return input_value


def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


def test_divisible_by_6(input_value):
    assert input_value % 6 == 0

# Fixtures can be parameterized to run the same test with different data.
@pytest.fixture(params=[('alia',35),('deepika',40)])
def user_data(self,request):
    return request.param

def test_user(self, user_data):
    name,age = user_data
    assert isinstance(name, str)
    assert isinstance(age, int)


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    request.cls.driver = driver  # Assign the driver to the test class
    yield driver
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestPy:
     def test_login(self,setup):
        self.driver = setup
        assert "Automation" in self.driver.title

