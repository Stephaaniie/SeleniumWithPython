import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def init_driver(request):
    options = Options()
    options.add_argument("start-maximized")
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    request.cls.driver = web_driver
    yield
    web_driver.quit()
