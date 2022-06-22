@register
Feature: Register
  
  Scenario: Registro
    Given Abro la aplicación
    And Presiono el botón Registrate
    When Selecciono el tipo de registro
    And Agrego los datos nombre apellido telefono correo contrasena
    Then Agrego DNI NTransporte NSeguro Direccion Fotos
    And Acepto el acuerdo y guardo 