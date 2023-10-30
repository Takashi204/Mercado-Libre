from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Ruta al controlador de Chrome. Reemplázala con la ubicación de tu controlador.
CHROME_DRIVER_PATH = 'C:\webdriver\chromedriver-win64\chromedriver.exe'

# URL de Mercado Libre
url = 'https://www.mercadolibre.cl/'




# Configuración del navegador
chrome_options = webdriver.ChromeOptions()

# Inicializar el navegador
driver = webdriver.Chrome(options=chrome_options)

# Abrir Mercado Libre
driver.get(url)

# Término de búsqueda con un máximo de 120 caracteres
search_query = 'a' * 120  # Esto creará una cadena de 120 caracteres "a"

# Encontrar el campo de búsqueda por su nombre
search_box = driver.find_element(By.NAME, 'as_word')

# Limitar el término de búsqueda a 120 caracteres
search_query = search_query[:120]

# Ingresar el término de búsqueda en el campo de búsqueda
search_box.send_keys(search_query)

# Realizar la búsqueda presionando la tecla Enter
search_box.send_keys(Keys.RETURN)

# Esperar a que se carguen los resultados (puedes ajustar este tiempo según sea necesario)
#driver.implicitly_wait(10)
time.sleep(20)




# Cerrar el navegador
driver.close()