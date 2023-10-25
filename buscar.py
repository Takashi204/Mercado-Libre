from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Ruta al controlador de Chrome
CHROME_DRIVER_PATH = 'C:\webdriver\chromedriver-win64'

# Término de búsqueda
search_query = 'iPhone 12'

# Configuración del navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Ejecutar el navegador en modo sin cabeza (sin interfaz gráfica)

# Inicializar el navegador
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)

try:
    # Abrir el sitio de Mercado Libre
    driver.get('https://www.mercadolibre.com')

    # Encontrar el campo de búsqueda y escribir el término de búsqueda
    search_box = driver.find_element('name', 'as_word')
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Esperar a que los resultados de búsqueda estén presentes
    driver.implicitly_wait(10)

    # Imprimir los títulos de los productos encontrados
    product_titles = driver.find_elements('class name', 'ui-search-item__title')
    for title in product_titles:
        print(title.text)

finally:
    # Cerrar el navegador al finalizar
    driver.quit()