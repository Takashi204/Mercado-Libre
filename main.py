from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Ruta al controlador de Chrome. Reemplázala con la ubicación de tu controlador.
CHROME_DRIVER_PATH = 'C:\webdriver\chromedriver-win64'

# URL de Mercado Libre
url = 'https://www.mercadolibre.com/'

# Término de búsqueda
search_query = 'iphone'

# Configuración del navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Ejecutar el navegador en modo sin cabeza (sin interfaz gráfica)

# Inicializar el navegador
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)

# Abrir Mercado Libre
driver.get(url)

# Encontrar el campo de búsqueda y escribir el término de búsqueda
search_box = driver.find_element(By.NAME, 'as_word')
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Esperar a que se carguen los resultados (puedes ajustar este tiempo según sea necesario)
driver.implicitly_wait(10)

# Obtener los títulos de los productos encontrados
product_titles = driver.find_elements(By.CLASS_NAME, 'ui-search-item__title"')

# Mostrar los títulos de los productos encontrados
for title in product_titles:
    print(title.text)

# Cerrar el navegador
driver.close()