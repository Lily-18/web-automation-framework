import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_pages.login_admin_page import login_admin_page


class Test_01_Admin_login:
    admin_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    invalid_username = "SSSAAA"

    def take_screenshot(self, test_name):
        """Save screenshot in the OrangeHRM/screenshots/ folder."""
        base_dir = os.path.dirname(os.path.abspath(__file__))  # current file path
        project_dir = os.path.abspath(os.path.join(base_dir, ".."))  # go up to OrangeHRM
        screenshots_dir = os.path.join(project_dir, "screenshots")  # full path to screenshots

        os.makedirs(screenshots_dir, exist_ok=True)  # create folder if not exists
        file_path = os.path.join(screenshots_dir, f"{test_name}.png")
        self.driver.save_screenshot(file_path)
        print(f"Screenshot saved: {file_path}")

    def test_title_verification(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        actual_title = self.driver.title
        expected_title = "OrangeHRM"

        if actual_title == expected_title:
            assert True
        else:
            self.take_screenshot("test_title_verification")
            assert False

    def test_valid_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = login_admin_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()

        dashboard_heading = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )

        if dashboard_heading.text == "Dashboard":
            assert True
        else:
            self.take_screenshot("test_valid_admin_login")
            assert False

    def test_invalid_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = login_admin_page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='Invalid credentials']"))
        )

        if error_message.text == "Invalid credentials":
            assert True
        else:
            self.take_screenshot("test_invalid_admin_login")
            assert False
