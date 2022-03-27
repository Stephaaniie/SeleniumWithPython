from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By
from utils import get_web_driver

browser = 'chrome' 
driver = get_web_driver(browser)

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444",
            options=driver
    )

    def test_search_in_python_org(self):
        for i in range(0, 10):
            driver = self.driver
            driver.get("http://www.python.org")
            driver.implicitly_wait(60)
            self.assertIn("Python", driver.title)
            elem = driver.find_element(By.ID, "id-search-field")
            elem.send_keys("pycon")
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()