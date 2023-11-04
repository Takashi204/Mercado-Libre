import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time  # Importar el módulo time

class PruebaMercadoLibre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.mercadolibre.cl")
        self.driver.maximize_window()

    def test_ofertas_link(self):
        try:
            enlace_ofertas = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://www.mercadolibre.cl/ofertas#nav-header"]'))
            )
            enlace_ofertas.click()

            # Esperar 25 segundos después de hacer clic en el enlace "Ofertas"
            time.sleep(15)

            # Continuar con las siguientes acciones aquí
            # ...

            self.assertTrue(True, "Clic en Ofertas exitoso.")
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