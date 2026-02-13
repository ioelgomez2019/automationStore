"""
Step Definitions para Login
Este archivo contiene la implementación de los pasos definidos en el archivo .feature
Conecta el lenguaje Gherkin con el código Python usando Page Objects
"""
from behave import given, when, then
from pages.login_page import LoginPage
import time


# ==================== GIVEN (Dado) ====================

@given('que el usuario está en la página de login de SauceDemo')
def step_user_on_login_page(context):
    """
    Paso: El usuario está en la página de login
    Abre el navegador y navega a la página de login
    """
    print("\n🌐 Navegando a la página de login...")
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    time.sleep(1)
    print(f"✓ Página cargada: {context.login_page.URL}")


# ==================== WHEN (Cuando) ====================

@when('el usuario ingresa el nombre de usuario "{username}"')
def step_enter_username(context, username):
    """
    Paso: Ingresar nombre de usuario
    
    Args:
        username: Nombre de usuario a ingresar
    """
    print(f"👤 Ingresando usuario: {username}")
    context.login_page.enter_username(username)
    time.sleep(0.5)


@when('el usuario ingresa la contraseña "{password}"')
def step_enter_password(context, password):
    """
    Paso: Ingresar contraseña
    
    Args:
        password: Contraseña a ingresar
    """
    print(f"🔑 Ingresando contraseña: {'*' * len(password)}")
    context.login_page.enter_password(password)
    time.sleep(0.5)


@when('el usuario hace clic en el botón de login')
def step_click_login_button(context):
    """
    Paso: Hacer clic en el botón de login
    """
    print("🖱️  Haciendo clic en el botón de Login...")
    context.login_page.click_login_button()
    time.sleep(1)


@when('el usuario deja el campo de usuario vacío')
def step_leave_username_empty(context):
    """
    Paso: Dejar el campo de usuario vacío (no hace nada)
    """
    print("⊗ Campo de usuario dejado vacío")
    pass


@when('el usuario deja el campo de contraseña vacío')
def step_leave_password_empty(context):
    """
    Paso: Dejar el campo de contraseña vacío (no hace nada)
    """
    print("⊗ Campo de contraseña dejado vacío")
    pass


# ==================== THEN (Entonces) ====================

@then('el usuario debería ver la página de productos')
def step_should_see_products_page(context):
    """
    Paso: Verificar que se muestra la página de productos
    """
    print("✓ Verificando que el login fue exitoso...")
    is_successful = context.login_page.is_login_successful()
    assert is_successful, "❌ Error: No se encontró la página de productos"
    print("✓ Login exitoso - Página de productos visible")


@then('el título de la página debería ser "{expected_title}"')
def step_verify_page_title(context, expected_title):
    """
    Paso: Verificar el título de la página
    
    Args:
        expected_title: Título esperado de la página
    """
    print(f"✓ Verificando título de página...")
    actual_title = context.login_page.get_products_title()
    print(f"   Título esperado: {expected_title}")
    print(f"   Título obtenido: {actual_title}")
    assert actual_title.upper() == expected_title.upper(), \
        f"❌ El título no coincide. Esperado: '{expected_title}', Obtenido: '{actual_title}'"
    print("✓ Título verificado correctamente")


@then('el usuario debería ver un mensaje de error')
def step_should_see_error_message(context):
    """
    Paso: Verificar que se muestra un mensaje de error
    """
    print("✓ Verificando mensaje de error...")
    is_error_displayed = context.login_page.is_error_message_displayed()
    assert is_error_displayed, "❌ Error: No se encontró el mensaje de error esperado"
    
    error_message = context.login_page.get_error_message()
    context.error_message = error_message  # Guardar para validaciones posteriores
    print(f"✓ Mensaje de error encontrado: '{error_message}'")


@then('el mensaje de error debería contener "{expected_text}"')
def step_verify_error_message_contains(context, expected_text):
    """
    Paso: Verificar que el mensaje de error contiene un texto específico
    
    Args:
        expected_text: Texto que debe estar contenido en el mensaje de error
    """
    print(f"✓ Verificando contenido del mensaje de error...")
    
    # Obtener el mensaje de error si no está guardado
    if not hasattr(context, 'error_message'):
        context.error_message = context.login_page.get_error_message()
    
    error_message = context.error_message
    print(f"   Texto esperado: '{expected_text}'")
    print(f"   Mensaje completo: '{error_message}'")
    
    assert expected_text.lower() in error_message.lower(), \
        f"❌ El mensaje de error no contiene '{expected_text}'. Mensaje actual: '{error_message}'"
    
    print(f"✓ Mensaje de error verificado correctamente")


@then('el resultado del login debería ser "{expected_result}"')
def step_verify_login_result(context, expected_result):
    """
    Paso: Verificar el resultado del login (exitoso o error)
    Usado en escenarios parametrizados
    
    Args:
        expected_result: Resultado esperado ('exitoso' o 'error')
    """
    print(f"✓ Verificando resultado del login: {expected_result}")
    
    if expected_result.lower() == "exitoso":
        is_successful = context.login_page.is_login_successful()
        assert is_successful, \
            f"❌ Se esperaba login exitoso pero falló"
        print("✓ Login exitoso confirmado")
    
    elif expected_result.lower() == "error":
        is_error = context.login_page.is_error_message_displayed()
        assert is_error, \
            f"❌ Se esperaba un error pero el login fue exitoso"
        error_message = context.login_page.get_error_message()
        print(f"✓ Error confirmado: '{error_message}'")
    
    else:
        raise ValueError(f"Resultado no válido: {expected_result}. Use 'exitoso' o 'error'")
