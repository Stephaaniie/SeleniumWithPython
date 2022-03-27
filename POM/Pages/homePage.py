
from Config.locators import Locators

from Pages.basePage import BasePage

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.google.com/")

    def search(self, text):
        element = super().findElement(By.NAME, Locators.textBoxSearch_name)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)