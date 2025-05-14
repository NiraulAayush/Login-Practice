import pytest
from pages.login_page import Login
from data import login_credentials

URL = "http://testphp.vulnweb.com/login.php"

def test_login_valid_user(driver):
    login_page = Login(driver)
    login_page.load(URL)
    login_page.login(login_credentials.valid_credentials['username'], login_credentials.valid_credentials['password'])
    assert "userinfo.php" in driver.current_url.lower()

def test_login_invalid_user(driver):
    login_page = Login(driver)
    login_page.load(URL)
    login_page.login(login_credentials.invalid_credentials['username'],login_credentials.invalid_credentials['password'])

    assert "login.php" in driver.current_url.lower()

