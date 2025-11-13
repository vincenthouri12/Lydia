from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PopupPage:
    CONTAINER = (By.XPATH, '//android.widget.LinearLayout[@resource-id="org.wikipedia.alpha:id/container"]')
    CLOSE_BTN = (By.XPATH, '//android.widget.ImageView[@content-desc="Close"]')

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.timeout = timeout

    def close_popup_if_present(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(self.CONTAINER)
            )
            print("Popup détecté, fermeture en cours...")
            self.driver.find_element(*self.CLOSE_BTN).click()
            print("Popup fermé")
        except TimeoutException:
            print("ℹAucun popup détecté, on continue")
