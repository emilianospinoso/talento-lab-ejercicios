@unit @smoke
Feature: Multiplicación de enteros
  Para asegurar consistencia en el micro-servicio de cálculo
  Quiero verificar que la función multiplicar devuelve el producto correcto

  Scenario Outline: Producto <a> x <b>
    When multiplico <a> y <b>
    Then obtengo <resultado>

    Examples:
      | a | b | resultado |
      | 2 | 3 | 6 |
      | 5 | 0 | 0 |
      | 7 | 4 | 28 |
      | -2 | 3 | -6 |

  Scenario: Suma básica
    When sumo 5 y 3
    Then obtengo 8