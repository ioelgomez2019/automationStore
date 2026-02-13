"""
Test con Múltiples Usuarios - Demostración del POM
Prueba el login con diferentes usuarios para ver casos exitosos y fallidos
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import time

print("\n" + "="*70)
print("🧪 TEST CON MÚLTIPLES USUARIOS")
print("="*70 + "\n")

# Lista de usuarios a probar
usuarios_prueba = [
    {
        "nombre": "Usuario Estándar",
        "username": "standard_user",
        "password": "secret_sauce",
        "esperado": "exitoso"
    },
    {
        "nombre": "Usuario Bloqueado",
        "username": "locked_out_user",
        "password": "secret_sauce",
        "esperado": "error"
    },
    {
        "nombre": "Credenciales Inválidas",
        "username": "usuario_invalido",
        "password": "password_incorrecto",
        "esperado": "error"
    },
    {
        "nombre": "Usuario con Problemas",
        "username": "problem_user",
        "password": "secret_sauce",
        "esperado": "exitoso"
    }
]

# Configurar Chrome
options = Options()
options.add_argument("--start-maximized")

resultados = []

for i, usuario in enumerate(usuarios_prueba, 1):
    print(f"\n{'='*70}")
    print(f"🧪 TEST {i}/{len(usuarios_prueba)}: {usuario['nombre']}")
    print(f"{'='*70}\n")
    
    # Abrir navegador para cada test
    print("   🌐 Abriendo navegador...")
    driver = webdriver.Chrome(options=options)
    
    try:
        # Crear Page Object
        login_page = LoginPage(driver)
        
        # Ir a la página
        print("   📄 Cargando página...")
        login_page.open()
        time.sleep(1)
        
        # Ingresar credenciales
        print(f"   👤 Usuario: {usuario['username']}")
        print(f"   🔑 Contraseña: {'*' * len(usuario['password'])}")
        
        login_page.enter_username(usuario['username'])
        time.sleep(0.5)
        login_page.enter_password(usuario['password'])
        time.sleep(0.5)
        
        # Click en login
        print("   🖱️  Click en Login...")
        login_page.click_login_button()
        time.sleep(2)
        
        # Verificar resultado
        print("   🔍 Verificando resultado...\n")
        
        if login_page.is_login_successful():
            resultado = "exitoso"
            print("   ✅ LOGIN EXITOSO")
            print(f"   📊 Página: {login_page.get_products_title()}")
        else:
            resultado = "error"
            if login_page.is_error_message_displayed():
                error_msg = login_page.get_error_message()
                print("   ❌ LOGIN FALLÓ")
                print(f"   💬 Mensaje: {error_msg}")
            else:
                print("   ⚠️  Estado desconocido")
        
        # Comparar con esperado
        esperado = usuario['esperado']
        if resultado == esperado:
            print(f"   🎯 RESULTADO: ✅ PASS (Se esperaba {esperado}, obtuvo {resultado})")
            resultados.append({
                "usuario": usuario['nombre'],
                "resultado": "PASS"
            })
        else:
            print(f"   🎯 RESULTADO: ❌ FAIL (Se esperaba {esperado}, obtuvo {resultado})")
            resultados.append({
                "usuario": usuario['nombre'],
                "resultado": "FAIL"
            })
        
        time.sleep(2)
        
    except Exception as e:
        print(f"   ❌ ERROR en el test: {str(e)}")
        resultados.append({
            "usuario": usuario['nombre'],
            "resultado": "ERROR"
        })
    
    finally:
        driver.quit()
        print("   🔒 Navegador cerrado")

# Mostrar resumen
print("\n" + "="*70)
print("📊 RESUMEN DE RESULTADOS")
print("="*70 + "\n")

for i, res in enumerate(resultados, 1):
    icono = "✅" if res['resultado'] == "PASS" else "❌" if res['resultado'] == "FAIL" else "⚠️"
    print(f"   {i}. {icono} {res['usuario']}: {res['resultado']}")

total = len(resultados)
passed = sum(1 for r in resultados if r['resultado'] == "PASS")
failed = sum(1 for r in resultados if r['resultado'] == "FAIL")
errors = sum(1 for r in resultados if r['resultado'] == "ERROR")

print(f"\n   📈 Total: {total} | ✅ PASS: {passed} | ❌ FAIL: {failed} | ⚠️ ERROR: {errors}")

if failed == 0 and errors == 0:
    print("\n   🎉 ¡TODOS LOS TESTS PASARON!")
else:
    print(f"\n   ⚠️  Revisar {failed + errors} test(s) fallido(s)")

print("\n" + "="*70)

input("\nPresiona ENTER para salir...")
