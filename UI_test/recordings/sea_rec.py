from seleniumbase import BaseCase


class RecorderTests(BaseCase):
    def test_recording(self):
        self.open("https://test-moviltruck.azurewebsites.net/#/")
        self.open("https://test-moviltruck.azurewebsites.net/#/")
        self.click("mat-select#mat-select-0 > div > div")
        self.click("mat-option#mat-option-1 span")
        self.click("mat-select#mat-select-1 div span span")
        self.click("mat-option#mat-option-3 span")
        self.click('input[placeholder="Origen"]')
        self.type('input[placeholder="Origen"]', "Nueva Granada, Caracas")
        try:
            self.js_click("body > div:nth-child(12) > div:nth-child(1)")
        except:
            print("An exception occurred")
        #self.click('body > div:nth-child(12) > div:nth-child(1)')
        self.type('input[placeholder="Destino"]', "Av. Loira Arriba, Caracas")
        self.click("app-home-landing.ng-star-inserted mat-drawer-container mat-drawer-content div div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(5) button mat-icon")
