@ui @smoke
Feature: Login en SauceDemo
  El visitante debe poder autenticarse con credenciales válidas.

  Background:
    Given el navegador abre la página de login

  Scenario: Credenciales válidas
    When ingreso usuario "standard_user" y clave "secret_sauce"
    Then la URL contiene "inventory.html"

