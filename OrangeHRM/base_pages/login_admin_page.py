from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login_admin_page:
    textbox_username_name = "//input[@name='username']"
    textbox_password_name = "//input[@name='password']"
    textbox_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_username_name))
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_password_name))
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.textbox_login_xpath))
        )
        login_button.click()
