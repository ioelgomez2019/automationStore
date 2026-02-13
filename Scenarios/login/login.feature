# language: es
@login @smoke
Característica: Login en SauceDemo
  Como usuario de SauceDemo
  Quiero poder iniciar sesion en la plataforma
  Para acceder a las funcionalidades del sistema

  @exitoso @critical
  Esquema del escenario: proceso de login exitoso
    Dado abre la aplicacion
    Y el usuario inicia sesion con perfil "<perfil>" y es responsable de caja de tipo "<tipo>"
    Entonces el usuario deberia ver la pagina de productos

    Ejemplos:
      | perfil        | tipo   |
      | standard_user | normal |
