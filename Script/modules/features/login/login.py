from Script.modules.features.login.loginPage import LoginPage
from Script.modules.data.loginData import PASSWORD_VALIDA


class Login:
    
    def __init__(self, context):
        self.context = context
        self.driver = context.driver
        self.login_page = LoginPage(self.driver)
        self.esResponsableCaja = None
    
    def prepararScenario(self):
        return None
    
    def abrirAplicacion(self):
        self.login_page.open()
    
    def loginPorPerfil(self, perfil):
        username = perfil
        password = PASSWORD_VALIDA
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
    
    def ingresarCore(self):
        return None
