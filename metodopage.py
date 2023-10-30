from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Inicializar el navegador Chrome
CHROME_DRIVER = 'C:\webdriver\chromedriver-win64\chromedriver.exe'

url = 'https://www.mercadolibre.cl'


# Configuración del navegador
chrome_options = webdriver.ChromeOptions()

# Inicializar el navegador
driver = webdriver.Chrome(options=chrome_options)

# Abrir Mercado Libre
driver.get(url)
try:
    # Encontrar el campo de búsqueda y buscar un producto (por ejemplo, "iPhone 13")
    search_box = driver.find_element(By.NAME, 'as_word')
    search_box.send_keys('iPhone 13')
    search_box.submit()

    # Esperar hasta que los resultados de búsqueda estén presentes (máximo 10 segundos de espera)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ui-search-result__image'))
    )

    # Seleccionar el primer producto de los resultados de búsqueda
    primer_producto = driver.find_element(By.CLASS_NAME, 'ui-search-result__image')
    primer_producto.click()

    # Esperar hasta que la página del producto se cargue completamente (máximo 10 segundos de espera)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ui-pdp-title'))
    )

    # Esperar hasta que el enlace "Ver los medios de pago" esté presente en el DOM (máximo 10 segundos de espera)
    boton_ver_medios_de_pago = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ui-pdp-action-modal__link'))
    )

    # Hacer clic en el enlace "Ver los medios de pago"
    boton_ver_medios_de_pago.click()


    
except Exception as e:
    print(f'Error: {e}')


time.sleep(15)

driver.close()