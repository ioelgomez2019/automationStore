from Script.modules.config.environment import create_driver
from Script.modules.features.login.login import Login


def main():
    driver = create_driver()
    try:
        class Context:
            pass
        context = Context()
        context.driver = driver
        login = Login(context)
        login.prepararScenario()
        login.abrirAplicacion()
        login.loginPorPerfil("standard_user")
        login.ingresarCore()
        is_successful = login.login_page.is_login_successful()
        if not is_successful:
            raise AssertionError("Error: No se encontró la página de productos")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
