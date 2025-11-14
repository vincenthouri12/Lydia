from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class CarouselPage:

    forward_btn = (By.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/fragment_onboarding_forward_button']")
    done_btn = (By.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/fragment_onboarding_done_button']")
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def handle_carousel(self):
        while True:
            try:
                forward = self.driver.find_element(*self.forward_btn)
                if forward.is_displayed():
                    forward.click()
                    print("Bouton 'Forward' cliqué")
                    time.sleep(1)
                else:
                    break
            except NoSuchElementException:
                break
        try:
            time.sleep(1)
            done = self.driver.find_element(*self.done_btn)
            done.click()
            print("Bouton 'Done' cliqué — carrousel terminé")
            time.sleep(1)
        except NoSuchElementException:
            print("Bouton 'Done' introuvable !")