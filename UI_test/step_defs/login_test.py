from pytest_bdd import scenarios, given, when, then, parsers
from .objects import *
import time
import pytest

# Scenarios 
scenarios('../features/login.feature')

PAGE = 'https://test-moviltruck.azurewebsites.net/'

@pytest.fixture
@given('Abro la aplicación')
def abro_la_aplicacion_moviltruck(sb):
    sb.get(PAGE)
    sb.is_valid_url("https://test-moviltruck.azurewebsites.net/#/")
    time.sleep(6)

@when('Presiono el botón Login')
def presion_el_boton_login(sb):
    sb.execute_script(Login.LoginOpen)
    time.sleep(2)

@then(parsers.parse('Agrego los datos {Email} {Password} y presiono el botón de iniciar sesión'))
def agrego_los_datos_y_guardo (sb,Email,Password):
    sb.type("#email", Email)
    sb.type('#password', Password)
    #presiono el boton para inicar sesión
    sb.execute_script(Login.LoginButton)
    sb.is_valid_url("https://test-moviltruck.azurewebsites.net/#/")
    time.sleep(8)
