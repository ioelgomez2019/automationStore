# language: es
@checkout @smoke
Característica: Compra en SauceDemo
  Como usuario de SauceDemo
  Quiero completar una compra
  Para confirmar el pedido

  @exitoso @critical
  Esquema del escenario: compra exitosa
    Dado el usuario inicia sesion con "<usuario>" y "<password>"
    Cuando agrega los productos "<producto1>" y "<producto2>"
    Y hace click en el carrito de compra
    Y hace click en checkout
    Y completa el formulario con "<nombre>", "<apellido>", "<zip>"
    Y hace click en continue
    Y verifica las compras
    Y hace click en finish que finaliza la compra
    Entonces deberia ver la confirmacion "Thank you for your order!"

    Ejemplos:
      | usuario       | password     | producto1             | producto2               | nombre | apellido | zip   |
      | standard_user | secret_sauce | Sauce Labs Backpack   | Sauce Labs Bike Light   | Joel   | Santos   | 21005 |
