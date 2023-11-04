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

    def test_busqueda_con_caracteres_largos(self):
        try:
            # Término de búsqueda con más de 120 caracteres
            search_query = 'a' * 121  # Esto creará una cadena de 121 caracteres "a"

            # Encontrar el campo de búsqueda por su nombre
            search_box = self.driver.find_element(By.NAME, 'as_word')

            # Ingresar el término de búsqueda en el campo de búsqueda
            search_box.send_keys(search_query)

            # Realizar la búsqueda presionando la tecla Enter
            search_box.send_keys(Keys.RETURN)

            # Esperar a que se cargue la página de resultados (espera explícita de 10 segundos)
            time.sleep(10)

            # Verificar si se muestra un mensaje de error por exceder el límite de caracteres
            error_message = self.driver.find_element(By.CLASS_NAME, 'ui-search-no-result__text').text
            expected_error_message = "Por favor, ingresa menos de 120 caracteres"
            self.assertEqual(error_message, expected_error_message, "Mensaje de error incorrecto.")

        except Exception as e:
            self.assertTrue(False, f"Error inesperado: {e}")

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
            f.write("\nLa prueba fue fallida.\n")