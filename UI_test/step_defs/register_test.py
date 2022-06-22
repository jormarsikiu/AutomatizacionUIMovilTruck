from pytest_bdd import scenarios, given, when, then, parsers
from .objects import *
import time
import pytest
import random
import os


# Scenarios 
scenarios('../features/register.feature')
nombre = 'Automation'+str(random.randint(0,100))
apellido = 'TestUi'+str(random.randint(0,100))
phone = random.randint(1000000000,9000000000)
email = 'automationuimt'+str(random.randint(0,100))+'@gmail.com'
dni = random.randint(1000000000,9000000000)
nroT = random.randint(1000000000,9000000000)
seguro = random.randint(1000000000,9000000000)

PAGE = 'https://test-moviltruck.azurewebsites.net/'

@pytest.fixture
@given('Abro la aplicación')
def abro_la_aplicacion_moviltruck(sb):
    sb.get(PAGE)
    sb.is_valid_url("https://test-moviltruck.azurewebsites.net/#/")
    time.sleep(6)
 

@given('Presiono el botón Registrate')
def presion_el_boton_registrarse(sb):
    sb.execute_script(Register.RegisterButton)
    time.sleep(5)

@when('Selecciono el tipo de registro')
def agrego_tipo(sb):
    sb.execute_script(Register.RegisterTypeAnonimo)


@when('Agrego los datos nombre apellido telefono correo contrasena')
def agrego_los_datos_y_guardo (sb):
    
    sb.type("#fullName", nombre)
    sb.type('#nroT22', apellido)
    sb.type('#phoneNumber', phone)
    sb.type('#email11', email)
    sb.type('#pass', 'Pa$$w0rd')
    time.sleep(2)
    sb.execute_script(Register.NextButton)

@then('Agrego DNI NTransporte NSeguro Direccion Fotos')
def agrego_los_datos_continuacion_y_guardo (sb):
    
    sb.type("#dni", dni)
    sb.type("#nroT", nroT)
    sb.type("#email233", seguro)
    sb.click('#email')
    time.sleep(2)
    sb.type(".search.pac-target-input", 'Caracas')
    time.sleep(2)
    sb.click('div:contains("Distrito Capital, Venezuela")')
    time.sleep(2)
    sb.execute_script(Register.AceptButton)
    time.sleep(5)
    sb.execute_script(Register.NextButton)
    time.sleep(5)

    dir_name = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_name, "example_logs/%s" % "screenshot.png")
    sb.choose_file("div.right-side form div:nth-of-type(4) div ngx-file-drop div input", file_path)
    time.sleep(2)
    sb.choose_file("div.right-side form div:nth-of-type(4) div:nth-of-type(2) ngx-file-drop div input", file_path)
    time.sleep(2)
    sb.choose_file("div.right-side form div:nth-of-type(4) div:nth-of-type(3) ngx-file-drop div input", file_path)
    time.sleep(2)
    sb.execute_script(Register.NextButton)
    time.sleep(2)
    sb.choose_file("div.right-side form div:nth-of-type(5) div:nth-of-type(1) ngx-file-drop div input", file_path)
    time.sleep(2)
    sb.choose_file("div.right-side form div:nth-of-type(5) div:nth-of-type(2) ngx-file-drop div input", file_path)
    time.sleep(2)


@then('Acepto el acuerdo y guardo')
def agrego_los_datos_continuacion_y_guardo (sb):
    
    sb.execute_script(Register.AcceptPolicy)
    time.sleep(2)
    sb.execute_script(Register.NextButton)
    time.sleep(8)
    sb.is_valid_url("https://test-moviltruck.azurewebsites.net/#/login")           
               