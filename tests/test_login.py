"""
Test Login - Casos de prueba para la funcionalidad de login
"""
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
import time


class TestLogin(unittest.TestCase):
    """Clase de pruebas para la funcionalidad de login"""
    
    @classmethod
    def setUpClass(cls):
        """Configuración inicial antes de ejecutar todas las pruebas"""
        print("\n=== Iniciando Suite de Pruebas de Login ===\n")
    
    def setUp(self):
        """Configuración antes de cada prueba - Se ejecuta antes de cada test"""
        print(f"\n--- Iniciando prueba: {self._testMethodName} ---")
        
        # Configurar opciones de Chrome
        chrome_options = Options()
        # Descomenta la siguiente línea si quieres ejecutar en modo headless (sin interfaz gráfica)
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        
        # Inicializar el driver de Chrome
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        
        # Configurar timeout implícito
        self.driver.implicitly_wait(10)
        
        # Inicializar la página de login
        self.login_page = LoginPage(self.driver)
        
        # Abrir la página de login
        print("Abriendo el navegador Chrome...")
        self.login_page.open()
        print(f"Navegando a: {self.login_page.URL}")
        time.sleep(1)  # Pequeña pausa para visualizar
    
    def tearDown(self):
        """Limpieza después de cada prueba - Se ejecuta después de cada test"""
        print(f"--- Finalizando prueba: {self._testMethodName} ---")
        time.sleep(2)  # Pausa para visualizar el resultado
        
        # Cerrar el navegador
        if self.driver:
            print("Cerrando el navegador...")
            self.driver.quit()
    
    @classmethod
    def tearDownClass(cls):
        """Limpieza final después de ejecutar todas las pruebas"""
        print("\n=== Finalizando Suite de Pruebas de Login ===\n")
    
    def test_login_exitoso_usuario_standard(self):
        """
        Caso de prueba: Login exitoso con usuario standard_user
        Verifica que un usuario válido puede iniciar sesión correctamente
        """
        print("\n1. Ingresando credenciales válidas...")
        print("   Usuario: standard_user")
        print("   Contraseña: secret_sauce")
        
        # Ingresar credenciales válidas
        self.login_page.enter_username("standard_user")
        time.sleep(0.5)
        
        self.login_page.enter_password("secret_sauce")
        time.sleep(0.5)
        
        print("2. Haciendo click en el botón de Login...")
        self.login_page.click_login_button()
        time.sleep(1)
        
        # Verificar que el login fue exitoso
        print("3. Verificando que el login fue exitoso...")
        self.assertTrue(
            self.login_page.is_login_successful(),
            "El login no fue exitoso. No se encontró la página de productos."
        )
        
        # Verificar el título de la página de productos
        products_title = self.login_page.get_products_title()
        print(f"4. Título encontrado: '{products_title}'")
        self.assertEqual(
            products_title.upper(),
            "PRODUCTS",
            f"El título esperado era 'PRODUCTS', pero se encontró '{products_title}'"
        )
        
        # Verificar la URL actual
        current_url = self.login_page.get_current_url()
        print(f"5. URL actual: {current_url}")
        self.assertIn(
            "inventory.html",
            current_url,
            "La URL no contiene 'inventory.html'"
        )
        
        print("✓ Prueba exitosa: Login realizado correctamente")
    
    def test_login_con_metodo_completo(self):
        """
        Caso de prueba: Login usando el método login() completo
        Verifica el método login que realiza todo el proceso en una sola llamada
        """
        print("\n1. Realizando login con el método completo...")
        print("   Usuario: standard_user")
        print("   Contraseña: secret_sauce")
        
        # Usar el método login que hace todo el proceso
        self.login_page.login("standard_user", "secret_sauce")
        time.sleep(1)
        
        print("2. Verificando que el login fue exitoso...")
        self.assertTrue(
            self.login_page.is_login_successful(),
            "El login no fue exitoso"
        )
        
        print("✓ Prueba exitosa: Login realizado con método completo")
    
    def test_login_fallido_credenciales_invalidas(self):
        """
        Caso de prueba: Login fallido con credenciales inválidas
        Verifica que el sistema muestra un error con credenciales incorrectas
        """
        print("\n1. Ingresando credenciales inválidas...")
        print("   Usuario: usuario_invalido")
        print("   Contraseña: password_incorrecta")
        
        # Ingresar credenciales inválidas
        self.login_page.login("usuario_invalido", "password_incorrecta")
        time.sleep(1)
        
        print("2. Verificando que se muestra un mensaje de error...")
        self.assertTrue(
            self.login_page.is_error_message_displayed(),
            "No se mostró el mensaje de error esperado"
        )
        
        error_message = self.login_page.get_error_message()
        print(f"3. Mensaje de error encontrado: '{error_message}'")
        self.assertIn(
            "Username and password do not match",
            error_message,
            "El mensaje de error no es el esperado"
        )
        
        print("✓ Prueba exitosa: Se validó correctamente el error de login")
    
    def test_login_con_usuario_bloqueado(self):
        """
        Caso de prueba: Login con usuario bloqueado
        Verifica que el usuario locked_out_user no puede iniciar sesión
        """
        print("\n1. Intentando login con usuario bloqueado...")
        print("   Usuario: locked_out_user")
        print("   Contraseña: secret_sauce")
        
        self.login_page.login("locked_out_user", "secret_sauce")
        time.sleep(1)
        
        print("2. Verificando que se muestra un mensaje de error...")
        self.assertTrue(
            self.login_page.is_error_message_displayed(),
            "No se mostró el mensaje de error para usuario bloqueado"
        )
        
        error_message = self.login_page.get_error_message()
        print(f"3. Mensaje de error encontrado: '{error_message}'")
        self.assertIn(
            "locked out",
            error_message.lower(),
            "El mensaje de error no indica que el usuario está bloqueado"
        )
        
        print("✓ Prueba exitosa: Se validó correctamente el usuario bloqueado")
    
    def test_login_campos_vacios(self):
        """
        Caso de prueba: Login con campos vacíos
        Verifica que el sistema valida campos requeridos
        """
        print("\n1. Intentando login sin ingresar credenciales...")
        
        # Click directamente en login sin ingresar datos
        self.login_page.click_login_button()
        time.sleep(1)
        
        print("2. Verificando que se muestra un mensaje de error...")
        self.assertTrue(
            self.login_page.is_error_message_displayed(),
            "No se mostró el mensaje de error para campos vacíos"
        )
        
        error_message = self.login_page.get_error_message()
        print(f"3. Mensaje de error encontrado: '{error_message}'")
        self.assertIn(
            "Username is required",
            error_message,
            "El mensaje de error no indica que el usuario es requerido"
        )
        
        print("✓ Prueba exitosa: Se validó correctamente los campos requeridos")


if __name__ == "__main__":
    # Ejecutar las pruebas con verbosidad nivel 2 (detallado)
    unittest.main(verbosity=2)
