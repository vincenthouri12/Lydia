from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction 
from selenium.webdriver.common.actions.action_builder import ActionBuilder


import time

class CresusPage:
    PREVIEW_BTN = (By.ID, "org.wikipedia.alpha:id/link_preview_primary_button")
    CRESUS_TEXT = (By.XPATH, '(//android.widget.TextView[@text="Crésus"])[1]')
    CRESUS_XPATH = '//android.view.View[@content-desc="Crésus roi de Lydie et dernier souverain de la dynastie des Mermnades (vers 596-Vers 546 av. J.-C.)"]'

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def scroll(self):
        screeb_size = self.driver.get_window_size()
        start_x = screeb_size['width'] / 2
        start_y = screeb_size['height'] * 0.8
        end_y = screeb_size['height'] * 0.1

        actions = ActionChains(self.driver)
        pointer = PointerInput(interaction.POINTER_TOUCH, "finger")
        actions_builder = ActionBuilder(self.driver, mouse=pointer)
        actions_builder.pointer_action.move_to_location(x=int(start_x), y=int(start_y))
        actions_builder.pointer_action.pointer_down()
        actions_builder.pointer_action.move_to_location(x=int(start_x), y=int(end_y))
        actions_builder.pointer_action.pointer_up()
        actions.w3c_actions = actions_builder
        actions.perform()

    def scroll_to_crésus_and_click(self):

        MAX_SCROLLS = 40
        time.sleep(1) 

        for _ in range(MAX_SCROLLS):
            try:        
                elem = self.driver.find_element(By.XPATH, self.CRESUS_XPATH)
                if elem.is_displayed():
                    elem.click()
                    print("Lien Crésus cliqué")
                    return
            except NoSuchElementException:
                self.scroll()

        raise RuntimeError("Lien Crésus non trouvé après scroll")

    def click_preview_if_visible(self):
        try:
            btn = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(self.PREVIEW_BTN)
            )
            btn.click()
            print("Bouton Preview cliqué")
        except TimeoutException:
            print("ℹBouton Preview non visible, on continue")

    def verify_crésus_displayed(self):
        try:
            elem = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(self.CRESUS_TEXT)
            )
            assert elem.is_displayed(), "Le texte 'Crésus' n'est pas affiché !"
            print("Texte 'Crésus' vérifié")
        except (TimeoutException, AssertionError) as e:
            raise AssertionError(f"Vérification échouée : {e}")
