from behave import given, when, then
from Script.modules.features.checkout.checkout import Checkout


@given('el usuario inicia sesion con "{usuario}" y "{password}"')
def step_login(context, usuario, password):
    context.checkout = Checkout(context)
    context.checkout.iniciar_sesion(usuario, password)


@when('agrega los productos "{producto1}" y "{producto2}"')
def step_add_products(context, producto1, producto2):
    context.checkout.agregar_productos(producto1, producto2)


@when("visualiza el carrito")
def step_view_cart(context):
    context.checkout.ver_carrito()


@when("hace click en el carrito de compra")
def step_click_cart(context):
    context.checkout.ver_carrito()


@when("hace click en checkout")
def step_click_checkout(context):
    context.checkout.ir_a_checkout()


@when('completa el formulario con "{nombre}", "{apellido}", "{zip_code}"')
def step_fill_form(context, nombre, apellido, zip_code):
    context.checkout.completar_formulario(nombre, apellido, zip_code)


@when("hace click en continue")
def step_click_continue(context):
    context.checkout.continuar_checkout()


@when("verifica las compras")
def step_verify_overview(context):
    context.checkout.verificar_resumen_compra()


@when("finaliza la compra")
def step_finish(context):
    context.checkout.finalizar_compra()


@when("hace click en finish que finaliza la compra")
def step_finish_via_click(context):
    context.checkout.finalizar_compra()


@then('deberia ver la confirmacion "{mensaje}"')
def step_verify_confirmation(context, mensaje):
    actual = context.checkout.obtener_confirmacion()
    assert actual.strip() == mensaje, f"Confirmacion esperada: '{mensaje}', obtenida: '{actual}'"
