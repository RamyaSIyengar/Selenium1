import pytest


class TestClass:
    def test_loginbyemail(self):
        print("this is login by email")
        assert 1 == True

    def test_loginbyfacebook(self):
        print("Login by Facebook")
        assert 1 == 1

    def test_loginbygithub(self):
        print("Login by GitHub")

    @pytest.mark.skip
    def test_signupbyemail(self):
        print("SignUp by email")
        assert 2 == 2

    @pytest.mark.skip
    def test_signupbyfacebook(self):
        print("signup by Facebook")
        assert 1 == 1

    @pytest.mark.skip
    def test_signupbygithub(self):
        print("signup by GitHub")
