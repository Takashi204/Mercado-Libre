from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
from datetime import datetime

class PruebaMercadoLibre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.mercadolibre.cl')

    def test_ver_datos_vendedor(self):
        try:
            search_box = self.driver.find_element(By.NAME, 'as_word')
            search_box.send_keys('iPhone 13')
            search_box.submit()

            # Esperar hasta que los resultados de búsqueda estén presentes (máximo 10 segundos de espera)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ui-search-result__image'))
            )

            # Seleccionar el primer producto de los resultados de búsqueda
            primer_producto = self.driver.find_element(By.CLASS_NAME, 'ui-search-result__image')
            primer_producto.click()

            # Esperar hasta que la página del producto se cargue completamente (máximo 10 segundos de espera)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ui-pdp-title'))
            )

            # Hacer clic en "Ver más datos del vendedor"
            ver_datos_vendedor = self.driver.find_element(By.XPATH, "//a[contains(@href, 'MERCADOLIBRE+ELECTRONICA_CL') and @class='ui-pdp-media__action ui-box-component__action']")
            self.driver.execute_script("arguments[0].click();", ver_datos_vendedor)

            # Esperar 15 segundos después de hacer clic en el enlace
            time.sleep(15)

            # Realizar otras acciones si es necesario

            self.assertTrue(True, "Ver datos del vendedor exitoso.")
        except Exception as e:
            self.assertTrue(False, f"Error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    # Ejecutar las pruebas y generar un informe de texto
    test_suite = unittest.TestLoader().loadTestsFromTestCase(PruebaMercadoLibre)
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suite)

    # Generar un informe de texto con la fecha y hora actual
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"Informe_Prueba_{now}.txt"

    with open(report_file, "w") as f:
        f.write(f"Prueba realizada el {now}\n\n")
        f.write(f"Resultado: {'Éxito' if test_result.wasSuccessful() else 'Fallo'}\n")
        f.write(f"Total de pruebas: {test_result.testsRun}\n")
        f.write(f"Pruebas exitosas: {test_result.testsRun - len(test_result.failures) - len(test_result.errors)}\n")
        f.write(f"Pruebas fallidas: {len(test_result.failures)}\n")
        f.write(f"Errores: {len(test_result.errors)}\n")

        if len(test_result.failures) > 0:
            f.write("\nDetalles de las fallas:\n")
            for failure in test_result.failures:
                f.write(f"{failure[0]}\n")
                f.write(f"{failure[1]}\n\n")