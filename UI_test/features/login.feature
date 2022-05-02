@login
Feature: Login
  
  Scenario: Login
    Given Abro la aplicación
    When Presiono el botón Login
    Then Agrego los datos <Email> <Password> y presiono el botón de iniciar sesión

    Examples: userinfo
    |Email              |Password |
    |QA@corpalcione.com |Pa$$w0rd |

 