from selenium import webdriver

# Creo un diccionario donde vamos a guardar nuestros drivers disponibles
web_drivers = {
    'chrome': webdriver.ChromeOptions(),
    'edge': webdriver.EdgeOptions(),
    'firefox': webdriver.FirefoxOptions()
}

# Creo una funcion que me devuelva el driver segun el browser
def get_web_driver(browser):
    return web_drivers[browser] 
