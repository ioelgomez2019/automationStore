from Script.modules.features.login.login import Login
from Script.modules.features.checkout.inventoryPage import InventoryPage
from Script.modules.features.checkout.cartPage import CartPage
from Script.modules.features.checkout.checkoutPage import CheckoutPage


class Checkout:
    
    def __init__(self, context):
        self.context = context
        self.driver = context.driver
        self.login_logic = Login(context)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
    
    def iniciar_sesion(self, usuario, password):
        self.login_logic.prepararScenario()
        self.login_logic.abrirAplicacion()
        self.login_logic.loginConCredenciales(usuario, password)
        if not self.login_logic.login_page.is_login_successful():
            raise AssertionError("Login fallido: no se encontro la pagina de productos")
        self.inventory_page.wait_for_page()
    
    def agregar_productos(self, producto1, producto2):
        self.inventory_page.add_product_to_cart(producto1)
        self.inventory_page.add_product_to_cart(producto2)
    
    def ver_carrito(self):
        self.inventory_page.open_cart()

    def ir_a_checkout(self):
        self.cart_page.click_checkout()
    
    def completar_formulario(self, nombre, apellido, zip_code):
        self.checkout_page.fill_form(nombre, apellido, zip_code)

    def continuar_checkout(self):
        self.checkout_page.click_continue()

    def verificar_resumen_compra(self):
        title = self.checkout_page.get_page_title()
        assert title.strip() == "Checkout: Overview", \
            f"Resumen esperado: 'Checkout: Overview', obtenido: '{title}'"
    
    def finalizar_compra(self):
        self.checkout_page.click_finish()
    
    def obtener_confirmacion(self):
        return self.checkout_page.get_complete_header()
