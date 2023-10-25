from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Ruta al controlador de Chrome
CHROME_DRIVER_PATH = 'C:\webdriver\chromedriver-win64'

# URL del producto a comprar
product_url = 'https://articulo.mercadolibre.cl/MLC-2016871404-notebook-js-156-intel-celeron-16gb-ram-512gb-ssd-8000mah-_JM#polycard_client=recommendations_home_navigation-recommendations&reco_backend=machinalis-homes&reco_client=home_navigation-recommendations&reco_item_pos=1&reco_backend_type=function&reco_id=5ac8b3ca-d67e-4338-b415-f6dd0a7c1c79'

# Datos para la compra
nombre = 'Nombre Completo'
direccion = 'Dirección de Envío'
ciudad = 'Ciudad'
codigo_postal = 'Código Postal'
numero_tarjeta = 'Número de Tarjeta'
fecha_expiracion = 'Fecha de Expiración (MM/YY)'
codigo_cvc = 'Código de Seguridad CVC'

# Configuración del navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Ejecutar el navegador en modo sin cabeza (sin interfaz gráfica)

# Inicializar el navegador
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)

try:
    # Abrir la página del producto
    driver.get(product_url)

    # Hacer clic en el botón "Comprar"
    buy_button = driver.find_element('class name', 'andes-button__content')
    buy_button.click()

    # Llenar los detalles de la compra
    name_field = driver.find_element('name', 'nombre')
    name_field.send_keys(nombre)

    address_field = driver.find_element('name', 'direccion')
    address_field.send_keys(direccion)

    city_field = driver.find_element('name', 'ciudad')
    city_field.send_keys(ciudad)

    postal_code_field = driver.find_element('name', 'codigo_postal')
    postal_code_field.send_keys(codigo_postal)

    card_number_field = driver.find_element('name', 'numero_tarjeta')
    card_number_field.send_keys(numero_tarjeta)

    expiration_field = driver.find_element('name', 'fecha_expiracion')
    expiration_field.send_keys(fecha_expiracion)

    cvc_field = driver.find_element('name', 'codigo_cvc')
    cvc_field.send_keys(codigo_cvc)

    # Confirmar la compra (este paso puede variar según el sitio web)
    confirm_button = driver.find_element('class name', 'class_del_boton_confirmar')
    confirm_button.click()

    # Esperar a que la compra se complete (puede requerir confirmación adicional por correo electrónico, etc.)
    driver.implicitly_wait(30)

finally:
    # Cerrar el navegador al finalizar
    driver.quit()