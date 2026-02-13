"""
Test de Login Completo con POM
Este test hace login real en SauceDemo usando Page Objects
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import time

print("\n" + "="*70)
print("🔐 TEST DE LOGIN COMPLETO - SauceDemo")
print("="*70 + "\n")

# Configurar Chrome
options = Options()
options.add_argument("--start-maximized")

print("1️⃣  Abriendo Chrome...")
driver = webdriver.Chrome(options=options)

try:
    # Crear instancia del Page Object
    login_page = LoginPage(driver)
    
    # Paso 1: Ir a la página
    print("2️⃣  Navegando a SauceDemo...")
    login_page.open()
    time.sleep(2)
    print("   ✅ Página cargada\n")
    
    # Paso 2: Ingresar credenciales
    print("3️⃣  Ingresando credenciales...")
    username = "standard_user"
    password = "secret_sauce"
    
    print(f"   👤 Usuario: {username}")
    login_page.enter_username(username)
    time.sleep(1)
    
    print(f"   🔑 Contraseña: {'*' * len(password)}")
    login_page.enter_password(password)
    time.sleep(1)
    
    # Paso 3: Click en Login
    print("\n4️⃣  Haciendo click en botón Login...")
    login_page.click_login_button()
    time.sleep(2)
    
    # Paso 4: Verificar resultado
    print("5️⃣  Verificando resultado...\n")
    
    if login_page.is_login_successful():
        print("   " + "="*66)
        print("   ✅ ¡LOGIN EXITOSO!")
        print("   " + "="*66)
        print(f"   📄 Título de página: {login_page.get_products_title()}")
        print(f"   🔗 URL actual: {login_page.get_current_url()}")
        print("   " + "="*66)
    else:
        print("   " + "="*66)
        print("   ❌ LOGIN FALLÓ")
        print("   " + "="*66)
        
        if login_page.is_error_message_displayed():
            error = login_page.get_error_message()
            print(f"   ⚠️  Error: {error}")
        print("   " + "="*66)
    
    print("\n" + "="*70)
    print("✅ TEST COMPLETADO")
    print("="*70)
    
    print("\n⏸️  Esperando 5 segundos antes de cerrar...")
    time.sleep(5)
    
except Exception as e:
    print(f"\n❌ ERROR durante el test:")
    print(f"   {str(e)}")
    import traceback
    traceback.print_exc()

finally:
    print("\n6️⃣  Cerrando navegador...")
    driver.quit()
    print("   ✅ Navegador cerrado\n")

input("Presiona ENTER para salir...")
