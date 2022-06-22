@search
Feature: Search
  
  Scenario: Search
    Given Abro la web
    When Uso el buscador por <Rol> <Item>
    Then Selecciono Origen y Destino y presiono el boton buscar cargas
    And Uso el buscador dentro de la pagina principal

    Examples: info
    |Rol           |Item        | 
    |Transportista |Refrigerada |
    |Operador      |Seca        |
