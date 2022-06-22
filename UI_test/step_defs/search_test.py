from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenarios, given, when, then, parsers
from .objects import *
import time
import pytest

# Scenarios 
scenarios('../features/search.feature')

#Variables globales
PAGE = 'https://test-moviltruck.azurewebsites.net/'
Origen = 'Nueva Granada, Caracas'
Destino = 'La Urbina, Caracas'
Destino2 = 'Av. Loira Arriba, Caracas'
Fecha = '13/12/2022'

@pytest.fixture
@given('Abro la web')
def abro_la_aplicacion_moviltruck(sb):
    sb.get(PAGE)
    sb.is_valid_url("https://test-moviltruck.azurewebsites.net/#/")
    time.sleep(6)

@when(parsers.parse('Uso el buscador por {Rol} {Item}'))
def uso_el_buscador(sb, Rol, Item):
    if Rol == 'Transportista':
        time.sleep(5)
        sb.click_xpath(SearchHome.SelectTypeHome)
        sb.click_xpath(SearchHome.SelectTransportistaHome)
    elif  Rol == 'Operador':
        time.sleep(5)
        sb.click_xpath(SearchHome.SelectTypeHome)
        sb.click_xpath(SearchHome.SelectOperadorHome)
    else:
        print("ERROR")

    if Item == 'Refrigerada':
        time.sleep(5)
        sb.click_xpath(SearchHome.SelectItemHome)
        sb.click_xpath(SearchHome.SelectRefrigHome)
    elif Item == 'Seca':
        time.sleep(5)
        sb.click_xpath(SearchHome.SelectItemHome)
        sb.click_xpath(SearchHome.SelectSecaHome)
        time.sleep(2)
    else:
        print("ERROR")
    
@then('Selecciono Origen y Destino y presiono el boton buscar cargas')
def uso_el_buscador_presiono_enter(sb):
    sb.type(SearchHome.InputOrigenHome, Origen)
    time.sleep(2)
    element = sb.wait_for_element_visible(SearchHome.InputOrigenHome)
    element.send_keys(Keys.ARROW_DOWN)
    element.send_keys(Keys.ENTER)
    time.sleep(2)
    sb.type(SearchHome.InputDestinoHome, Destino)
    time.sleep(2)
    element2 = sb.wait_for_element_visible(SearchHome.InputDestinoHome)
    element2.send_keys(Keys.ARROW_DOWN)
    element2.send_keys(Keys.ENTER)
    time.sleep(2)
    sb.click_xpath(SearchHome.SearchButton)
    time.sleep(5)
    sb.is_valid_url("https://test-moviltruck.azurewebsites.net/#/system/fast-booking/")
    
@then('Uso el buscador dentro de la pagina principal')
def buscar_principal(sb):
    #Generador carga seca
    time.sleep(5)
    sb.click_xpath(SearchMain.SelectType)
    sb.click_xpath(SearchMain.SelectOperador)
    
    time.sleep(5)
    sb.click_xpath(SearchMain.SelectItem)
    sb.click_xpath(SearchMain.SelectSeca)
    time.sleep(5)
      
    sb.type(SearchMain.InputOrigen, Origen)    
    time.sleep(2)
    element = sb.wait_for_element_visible(SearchMain.InputOrigen)
    element.send_keys(Keys.ARROW_DOWN)
    element.send_keys(Keys.ENTER)
    time.sleep(2)
        
    sb.type(SearchMain.InputDestino, Destino2)
    time.sleep(2)
    element2 = sb.wait_for_element_visible(SearchMain.InputDestino)
    element2.send_keys(Keys.ARROW_DOWN)
    element2.send_keys(Keys.ENTER)
    time.sleep(2)

    sb.type(SearchMain.OpenCalendary, Fecha)
    sb.click_xpath(SearchMain.ButtonSearch)
    time.sleep(6)