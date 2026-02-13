from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import time

print("\n" + "="*70)
print("TEST DE LOGIN COMPLETO - SauceDemo")
print("="*70 + "\n")

options = Options()
options.add_argument("--start-maximized")

print("Abriendo Chrome...")
driver = webdriver.Chrome(options=options)

try:
    login_page = LoginPage(driver)
    
    print("Navegando a SauceDemo...")
    login_page.open()
    time.sleep(2)
    print("Pagina cargada\n")
    
    print("Ingresando credenciales...")
    username = "standard_user"
    password = "secret_sauce"
    
    print(f"Usuario: {username}")
    login_page.enter_username(username)
    time.sleep(1)
    
    print(f"Contrasena: {'*' * len(password)}")
    login_page.enter_password(password)
    time.sleep(1)
    
    print("\nHaciendo click en boton Login...")
    login_page.click_login_button()
    time.sleep(2)
    
    print("Verificando resultado...\n")
    
    if login_page.is_login_successful():
        print("   " + "="*66)
        print("   LOGIN EXITOSO")
        print("   " + "="*66)
        print(f"   Titulo de pagina: {login_page.get_products_title()}")
        print(f"   URL actual: {login_page.get_current_url()}")
        print("   " + "="*66)
    else:
        print("   " + "="*66)
        print("   LOGIN FALLO")
        print("   " + "="*66)
        
        if login_page.is_error_message_displayed():
            error = login_page.get_error_message()
            print(f"   Error: {error}")
        print("   " + "="*66)
    
    print("\n" + "="*70)
    print("TEST COMPLETADO")
    print("="*70)
    
    print("\nEsperando 5 segundos antes de cerrar...")
    time.sleep(5)
    
except Exception as e:
    print(f"\nERROR durante el test:")
    print(f"   {str(e)}")
    import traceback
    traceback.print_exc()

finally:
    print("\nCerrando navegador...")
    driver.quit()
    print("Navegador cerrado\n")

input("Presiona ENTER para salir...")
