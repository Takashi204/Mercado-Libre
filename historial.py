from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Ruta al controlador de Chrome. Reemplázala con la ubicación de tu controlador.
CHROME_DRIVER = 'C:\webdriver\chromedriver-win64\chromedriver.exe'

# URL de Mercado Libre
url = 'https://www.mercadolibre.cl'

# Configuración del navegador
chrome_options = webdriver.ChromeOptions()

# Inicializar el navegador
driver = webdriver.Chrome(options=chrome_options)

# Abrir Mercado Libre
driver.get(url)

try:
    # Encontrar el enlace "Historial" por su atributo href
    enlace_historial = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="navigation#nav-header"]'))
    )

    # Hacer clic en el enlace "Historial"
    enlace_historial.click()


except Exception as e:
    print(f'Error: {e}')







time.sleep(15)

driver.close()