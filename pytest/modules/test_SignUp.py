import pytest


class TestSignUp:

    def test_signupbyemail(self, setup):
        print("SignUp by email")
        assert 1 == True

    def test_signupbyfacebook(self, setup):
        print("signup by Facebook")
        assert 1 == 1

    def test_signupbygithub(self, setup):
        print("signup by GitHub")


# pytest -v -s pytest\modules\
# pytest -v -s .\pytest\modules\test_SignUp.py::TestSignUp::test_signupbyemail
