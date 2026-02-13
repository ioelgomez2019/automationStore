# language: es
@login @smoke
Característica: Login en SauceDemo
  Como usuario de SauceDemo
  Quiero poder iniciar sesion en la plataforma
  Para acceder a las funcionalidades del sistema

  @exitoso @critical
  Esquema del escenario: proceso de login exitoso
    Dado abre la aplicacion
    y el usuario ingresa su "<usuario>" y "<password>"
    Entonces el usuario deberia ver la pagina de productos

    Ejemplos:
      | usuario       | password     |
      | standard_user | secret_sauce |
