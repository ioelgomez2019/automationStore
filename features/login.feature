# language: es
# Archivo Feature - Define los escenarios de prueba en lenguaje Gherkin
# Este archivo describe el comportamiento esperado del sistema de login

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
    Y el usuario hace clic en el otón de login
    Entonces el usuario debería ver la página de productos
    Y el título de la página debería ser "PRODUCTS"

  @exitoso
  Escenario: Login exitoso con usuario problem_user
    Cuando el usuario ingresa el nombre de usuario "problem_user"
    Y el usuario ingresa la contraseña "secret_sauce"
    Y el usuario hace clic en el botón de login
    Entonces el usuario debería ver la página de productos

  @error @negative
  Escenario: Login fallido con credenciales inválidas
    Cuando el usuario ingresa el nombre de usuario "usuario_invalido"
    Y el usuario ingresa la contraseña "password_incorrecto"
    Y el usuario hace clic en el botón de login
    Entonces el usuario debería ver un mensaje de error
    Y el mensaje de error debería contener "Username and password do not match"

  @error @negative
  Escenario: Login con usuario bloqueado
    Cuando el usuario ingresa el nombre de usuario "locked_out_user"
    Y el usuario ingresa la contraseña "secret_sauce"
    Y el usuario hace clic en el botón de login
    Entonces el usuario debería ver un mensaje de error
    Y el mensaje de error debería contener "locked out"

  @validacion @negative
  Escenario: Login sin ingresar nombre de usuario
    Cuando el usuario deja el campo de usuario vacío
    Y el usuario ingresa la contraseña "secret_sauce"
    Y el usuario hace clic en el botón de login
    Entonces el usuario debería ver un mensaje de error
    Y el mensaje de error debería contener "Username is required"

  @validacion @negative
  Escenario: Login sin ingresar contraseña
    Cuando el usuario ingresa el nombre de usuario "standard_user"
    Y el usuario deja el campo de contraseña vacío
    Y el usuario hace clic en el botón de login
    Entonces el usuario debería ver un mensaje de error
    Y el mensaje de error debería contener "Password is required"

  @validacion @negative
  Escenario: Login sin ingresar credenciales
    Cuando el usuario deja el campo de usuario vacío
    Y el usuario deja el campo de contraseña vacío
    Y el usuario hace clic en el botón de login
    Entonces el usuario debería ver un mensaje de error
    Y el mensaje de error debería contener "Username is required"

  @parametrizado
  Esquema del escenario: Login con diferentes usuarios
    Cuando el usuario ingresa el nombre de usuario "<usuario>"
    Y el usuario ingresa la contraseña "<password>"
    Y el usuario hace clic en el botón de login
    Entonces el resultado del login debería ser "<resultado>"

    Ejemplos:
      | usuario                 | password     | resultado |
      | standard_user          | secret_sauce | exitoso   |
      | problem_user           | secret_sauce | exitoso   |
      | performance_glitch_user| secret_sauce | exitoso   |
      | locked_out_user        | secret_sauce | error     |
      | usuario_invalido       | pass_invalido| error     |
