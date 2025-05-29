@api
Feature: Posts JSONPlaceholder
  La API de posts debe permitir crear y borrar registros.

  Scenario: Crear y eliminar post
    When creo un post con title "BDD Test" y body "Contenido de prueba"
    Then la respuesta POST es 201 y contiene id
    When elimino el post recién creado
    Then la respuesta DELETE es 200
