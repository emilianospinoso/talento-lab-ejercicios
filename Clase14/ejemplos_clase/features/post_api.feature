@api
Feature: Posts JSONPlaceholder
  Como desarrollador quiero interactuar con la API de posts
  Para validar que el backend funciona correctamente

  Scenario: Crear y eliminar post
    When creo un post con title "BDD Test" y body "Contenido de prueba"
    Then la respuesta POST es 201 y contiene id
    When elimino el post recién creado
    Then la respuesta DELETE es 200

  Scenario: Obtener lista de posts
    When obtengo la lista de posts
    Then la respuesta GET es 200
    And la respuesta contiene al menos 1 post