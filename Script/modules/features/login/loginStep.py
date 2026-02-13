from behave import given, then
from Script.modules.features.login.login import Login


@given("abre la aplicacion")
def step_open_app(context):
    context.login_logic = Login(context)
    context.login_logic.prepararScenario()
    context.login_logic.abrirAplicacion()


@given('el usuario ingresa su "{usuario}" y "{password}"')
def step_login_profile(context, usuario, password):
    context.login_logic = Login(context)
    context.login_logic.prepararScenario()
    context.login_logic.abrirAplicacion()
    context.login_logic.loginConCredenciales(usuario, password)


@then("el usuario deberia ver la pagina de productos")
def step_verify_products(context):
    is_successful = context.login_logic.login_page.is_login_successful()
    assert is_successful, "Error: No se encontró la página de productos"
