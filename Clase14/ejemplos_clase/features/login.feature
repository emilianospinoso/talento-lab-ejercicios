@ui @smoke
Feature: Login en SauceDemo
  Como usuario quiero poder autenticarme con credenciales válidas
  Para acceder al sistema de inventario

  Background:
    Given el navegador abre la página de login

  Scenario: Credenciales válidas
    When ingreso usuario "standard_user" y clave "secret_sauce"
    Then la URL contiene "inventory.html"

  Scenario Outline: Credenciales inválidas
    When ingreso usuario "<usuario>" y clave "<clave>"
    Then aparece un mensaje de error

    Examples:
      | usuario | clave |
      | usuario_malo | secret_sauce |
      | standard_user | clave_mala |
      | locked_out_user | secret_sauce |