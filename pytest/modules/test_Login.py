import pytest


class TestLogin:

    def test_loginbyemail(self, setup):
        print("this is login by email")
        assert 1 == True

    def test_loginbyfacebook(self, setup):
        print("Login by Facebook")
        assert 1 == 1

    def test_loginbygithub(self, setup):
        print("Login by GitHub")



