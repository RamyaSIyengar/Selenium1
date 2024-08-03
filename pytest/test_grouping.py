import pytest


class TestClass:

    @pytest.mark.group1
    def test_loginbyemail(self):
        print("this is login by email")
        assert 1 == True

    @pytest.mark.group1
    def test_loginbyfacebook(self):
        print("Login by Facebook")
        assert 1 == 1

    @pytest.mark.group2
    @pytest.mark.group1
    def test_loginbygithub(self):
        print("Login by GitHub")

    @pytest.mark.group2
    @pytest.mark.group1
    def test_signupbyemail(self):
        print("SignUp by email")
        assert 2 == 2


    @pytest.mark.group2
    def test_signupbyfacebook(self):
        print("signup by Facebook")
        assert 1 == 1

    @pytest.mark.group2
    def test_signupbygithub(self):
        print("signup by GitHub")


# pytest -v -s -m "group1"  .\pytest\test_grouping.py
# pytest -v -s -m "not group2"  .\pytest\test_grouping.py
# pytest -v -s -m "group1 and  group2"  .\pytest\test_grouping.py
