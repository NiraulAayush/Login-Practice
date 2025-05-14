from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_input_name = "uname"
        self.password_input_name = "pass"
        self.login_btn_xpath = "//input[@type = 'submit' and contains(@value, 'login')]"

    def load(self, url):
        self.driver.get(url)

    def login(self, username, password):

        self.wait.until(
            EC.presence_of_element_located((By.NAME, self.username_input_name))
        ).send_keys(username)

        self.wait.until(
            EC.presence_of_element_located((By.NAME, self.password_input_name))
        ).send_keys(password)

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.login_btn_xpath))
        ).click()





