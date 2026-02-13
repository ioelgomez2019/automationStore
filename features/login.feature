# language: es
@login @smoke
Característica: Login en SauceDemo
  Como usuario de SauceDemo
  Quiero poder iniciar sesión en la plataforma
  Para acceder a las funcionalidades del sistema

  Antecedentes:
    Dado que el usuario está en la página de login de SauceDemo

  @exitoso @critical
  Escenario: Login exitoso con credenciales válidas
    Cuando el usuario ingresa el nombre de usuario "standard_user"
    Y el usuario ingresa la contraseña "secret_sauce"
    Y el usuario hace clic en el botón de login
    Entonces el usuario debería ver la página de productos
    Y el título de la página debería ser "PRODUCTS"
