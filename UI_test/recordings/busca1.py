from seleniumbase import BaseCase
import time


class RecorderTests(BaseCase):
    def test_recording(self):
        self.open("https://test-moviltruck.azurewebsites.net/#/system/fast-booking")
        
        self.click("mat-select#mat-select-1 div span span")
        self.click("mat-option#mat-option-11 span")
        self.click("mat-select#mat-select-2 div span span")
        self.click("mat-option#mat-option-13 span")
        #self.click('input[placeholder="Origen"]')
        ButtonOrigen = '/html/body/app-root/body/app-header-geral/mat-drawer-container/mat-drawer-content/div/app-fast-booking/div/div[1]/div/div[3]/div/div/input'
        self.type(ButtonOrigen, "Av. Nueva Granada, Caracas, Distrito Capital, Venezuela")
        self.type('input[placeholder="Destino"]', "Av. Loira Arriba, Caracas 1020, Distrito Capital, Venezuela")
        self.click('input[placeholder="No tenemos nada que mostrar"]')
        self.click('button[aria-label="Next month"]')
        self.click('button[aria-label="Next month"]')
        self.click('button[aria-label="Next month"]')
        self.click('button[aria-label="Next month"]')
        self.click('button[aria-label="Next month"]')
        self.click('button[aria-label="Next month"]')
        self.click('td[aria-label="12 de diciembre de 2022"] span')
        self.click("app-fast-booking.ng-star-inserted div div:nth-of-type(6) button mat-icon")
        time.sleep(6)
