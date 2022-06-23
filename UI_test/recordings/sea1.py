from seleniumbase import BaseCase
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class RecorderTests(BaseCase):
    def test_recording(self):
            self.open("https://test-moviltruck.azurewebsites.net/#/")
            time.sleep(5)
            self.click("mat-select#mat-select-0 > div > div")
            time.sleep(5)
            self.click("mat-option#mat-option-1 span")
            time.sleep(5)
            self.click("mat-select#mat-select-1 div span span")
            self.click("mat-option#mat-option-3 span")
            time.sleep(2)
            self.type('input[placeholder="Origen"]', "Nueva Granada, Caracas")
            time.sleep(2)
            element = self.wait_for_element_visible('input[placeholder="Origen"]')
            element.send_keys(Keys.ARROW_DOWN)
            element.send_keys(Keys.ENTER)
            time.sleep(2)
            self.type('input[placeholder="Destino"]', "La Urbina, Caracas")
            time.sleep(2)
            element2 = self.wait_for_element_visible('input[placeholder="Destino"]')
            element2.send_keys(Keys.ARROW_DOWN)
            element2.send_keys(Keys.ENTER)
            time.sleep(2)
            self.execute_script('document.querySelector(".btn.btn-orange.botoncito").click()') 
            #self.click("app-home-landing.ng-star-inserted mat-drawer-container mat-drawer-content div div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(5) button mat-icon")
            time.sleep(5)
            self.is_valid_url("https://test-moviltruck.azurewebsites.net/#/system/fast-booking/")
            time.sleep(5)
        
