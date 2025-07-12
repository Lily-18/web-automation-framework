import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver



@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


# @pytest.fixture(autouse=True)
# def setup(self):
#     self.driver = webdriver.Chrome()
#     self.driver.get(self.admin_page_url)
#     self.driver.maximize_window()
#     yield
#     self.driver.quit()