from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Ruta al controlador de Chrome. Reemplázala con la ubicación de tu controlador.
CHROME_DRIVER_PATH = 'C:\webdriver\chromedriver-win64\chromedriver.exe'

# URL de Mercado Libre
url = 'https://www.mercadolibre.cl/'


# Término de búsqueda
search_query = 'iphone 13'

# Configuración del navegador
chrome_options = webdriver.ChromeOptions()

# Inicializar el navegador
driver = webdriver.Chrome(options=chrome_options)

# Abrir Mercado Libre
driver.get(url)

# Encontrar el campo de búsqueda y escribir el término de búsqueda
search_box = driver.find_element(By.NAME, 'as_word')
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Esperar a que se carguen los resultados (puedes ajustar este tiempo según sea necesario)
#driver.implicitly_wait(10)
time.sleep(20)

# Cerrar el navegador
driver.close()