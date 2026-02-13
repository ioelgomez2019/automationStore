from behave import given, then
from Script.modules.features.login.login import Login


@given("abre la aplicacion")
def step_open_app(context):
    context.login_logic = Login(context)
    context.login_logic.prepararScenario()
    context.login_logic.abrirAplicacion()


@given('el usuario inicia sesion con perfil "{perfil}" y es responsable de caja de tipo "{tipoResponsableCaja}"')
def step_login_profile(context, perfil, tipoResponsableCaja):
    context.login_logic = Login(context)
    context.login_logic.prepararScenario()
    context.login_logic.abrirAplicacion()
    context.login_logic.esResponsableCaja = tipoResponsableCaja
    context.login_logic.loginPorPerfil(perfil)
    context.login_logic.ingresarCore()


@then("el usuario deberia ver la pagina de productos")
def step_verify_products(context):
    is_successful = context.login_logic.login_page.is_login_successful()
    assert is_successful, "Error: No se encontró la página de productos"
