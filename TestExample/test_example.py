from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By
from utils import get_web_driver

# Declaro el browser que quiero usar
browser = 'chrome' 

# Llamo a la funcion para que me traiga el driver que necesito
driver = get_web_driver(browser)

# Defino una clase que extiende TestCase, 
# y le asigno una funcion donde vamos a setear en donde se va a ejecutar
class PythonOrgSearch(unittest.TestCase):
    # setUp se corre antes de cada test
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444",
            options=driver
    )

    # Creo una funcion de test donde especifico que app va a testear
    def test_search_in_python_org(self):
        for i in range(0, 10):
            driver = self.driver
            driver.get("https://www.python.org")
            driver.implicitly_wait(20)
            self.assertIn("Python", driver.title)
            elem = driver.find_element(By.ID, "id-search-field")
            elem.send_keys("pycon")
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in driver.page_source

    # tearDown se invoca despues de cada test  
    def tearDown(self):
        self.driver.quit()

        print("Done")

    # El bloque final muestra una forma sencilla de ejecutar las pruebas. 
    # unittest.main() proporciona una interfaz de command-line para el script de prueba.
    if __name__ == "__main__":
        unittest.main()