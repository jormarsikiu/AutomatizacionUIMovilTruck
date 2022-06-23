class Login():
    LoginOpen = '''document.querySelectorAll("[href*='#/login']")[0].click();'''
    LoginButton = '''document.querySelector('.btn-lg').click();'''
    
class Register():
    RegisterButton = '''document.querySelectorAll("[href*='#/register-list']")[0].click();'''
    RegisterTypeAnonimo = '''document.querySelectorAll('.col-md-12:nth-child(2) >.tipos')[0].click();'''
    NextButton = '''document.querySelectorAll('.btn.btn-orange.btn-lg.btn-block.mt-4.ng-star-inserted')[0].click()'''
    AceptButton = '''document.querySelectorAll('.btn.btn-orange.btn-md.btn-block.wellbet')[0].click()'''
    AcceptPolicy = '''document.querySelectorAll('.mat-checkbox-background')[0].click()'''
    image1 = '''/html/body/app-root/body/app-register-transport/div[2]/form/div[4]/div[1]/div/ngx-file-drop/div/div/div'''
    
class SearchHome():
    SelectTypeHome = '''/html/body/app-root/body/app-home-landing/mat-drawer-container/mat-drawer-content/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/mat-form-field'''
    SelectOperadorHome = '''/html/body/div[4]/div[2]/div/div/div/mat-option[1]/span'''
    SelectTransportistaHome = '''/html/body/div[4]/div[2]/div/div/div/mat-option[2]/span'''
    SelectItemHome = '''/html/body/app-root/body/app-home-landing/mat-drawer-container/mat-drawer-content/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/mat-form-field'''
    SelectSecaHome = '''/html/body/div[4]/div[2]/div/div/div/mat-option[1]/span'''
    SelectRefrigHome = '''/html/body/div[4]/div[2]/div/div/div/mat-option[2]/span'''
    InputOrigenHome = '''/html/body/app-root/body/app-home-landing/mat-drawer-container/mat-drawer-content/div[1]/div/div[2]/div[2]/div[1]/div[3]/div/div/input'''
    InputDestinoHome = '''/html/body/app-root/body/app-home-landing/mat-drawer-container/mat-drawer-content/div[1]/div/div[2]/div[2]/div[1]/div[4]/div/div/input'''
    SearchButton = '''/html/body/app-root/body/app-home-landing/mat-drawer-container/mat-drawer-content/div[1]/div/div[2]/div[2]/div[1]/div[5]/button'''
    
class SearchMain():
    SelectType = '''/html/body/app-root/body/app-header-geral/mat-drawer-container/mat-drawer-content/div/app-fast-booking/div/div[1]/div/div[1]/div/mat-select'''
    SelectTransportista = '''/html/body/div[4]/div[2]/div/div/div/mat-option[2]/span'''
    SelectOperador = '''/html/body/div[4]/div[2]/div/div/div/mat-option[1]/span'''
    SelectItem = '''/html/body/app-root/body/app-header-geral/mat-drawer-container/mat-drawer-content/div/app-fast-booking/div/div[1]/div/div[2]/div/mat-select'''
    SelectSeca = '''/html/body/div[4]/div[2]/div/div/div/mat-option[1]/span'''
    SelectRefrig = '''/html/body/div[4]/div[2]/div/div/div/mat-option[2]/span'''
    InputOrigen = '''/html/body/app-root/body/app-header-geral/mat-drawer-container/mat-drawer-content/div/app-fast-booking/div/div[1]/div/div[3]/div/div/input'''
    InputDestino = '''/html/body/app-root/body/app-header-geral/mat-drawer-container/mat-drawer-content/div/app-fast-booking/div/div[1]/div/div[4]/div/div/input'''
    OpenCalendary = '''/html/body/app-root/body/app-header-geral/mat-drawer-container/mat-drawer-content/div/app-fast-booking/div/div[1]/div/div[5]/div/div/input'''
    ButtonSearch = '''/html/body/app-root/body/app-header-geral/mat-drawer-container/mat-drawer-content/div/app-fast-booking/div/div[1]/div/div[6]/button'''
    
    OpenModalCarga = '''/html/body/app-root/body/app-header-geral/mat-drawer-container/mat-drawer-content/div/app-fast-booking/div/div[2]/div[2]/div[1]/div/div'''