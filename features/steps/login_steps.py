from behave import given, when, then
from pages.login_page import LoginPage
import time


@given('que el usuario está en la página de login de SauceDemo')
def step_user_on_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    time.sleep(1)


@when('el usuario ingresa el nombre de usuario "{username}"')
def step_enter_username(context, username):
    context.login_page.enter_username(username)
    time.sleep(0.5)


@when('el usuario ingresa la contraseña "{password}"')
def step_enter_password(context, password):
    context.login_page.enter_password(password)
    time.sleep(0.5)


@when('el usuario hace clic en el botón de login')
def step_click_login_button(context):
    context.login_page.click_login_button()
    time.sleep(1)


@then('el usuario debería ver la página de productos')
def step_should_see_products_page(context):
    is_successful = context.login_page.is_login_successful()
    assert is_successful, "Error: No se encontró la página de productos"


@then('el título de la página debería ser "{expected_title}"')
def step_verify_page_title(context, expected_title):
    actual_title = context.login_page.get_products_title()
    assert actual_title.upper() == expected_title.upper(), \
        f"El título no coincide. Esperado: '{expected_title}', Obtenido: '{actual_title}'"
