from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
from datetime import datetime

class PruebaMercadoLibre(unittest.TestCase):
    def setUp(self):
        # Inicializar el navegador
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.mercadolibre.cl/')

    def test_buscar_producto(self):
        try:
            # Encontrar el campo de búsqueda y escribir el término de búsqueda
            search_box = self.driver.find_element(By.NAME, 'as_word')
            search_box.send_keys('iphone 13')
            search_box.send_keys(Keys.RETURN)

            # Esperar a que se carguen los resultados (20 segundos de espera)
            time.sleep(15)

            # Realizar otras acciones si es necesario

            self.assertTrue(True, "Búsqueda de producto exitosa.")
        except Exception as e:
            self.assertTrue(False, f"Error: {e}")

    def tearDown(self):
        # Cerrar el navegador
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
        else:
            f.write("\nLa prueba de busqueda de producto fue exitosa.\n")