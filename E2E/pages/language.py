from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LanguagePage:
    LANGUAGE_BTN = (By.XPATH, '//android.widget.TextView[@content-desc="Language"]')
    LOOP_BTN = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[3]/android.widget.Button')
    INPUT_FIELD = (By.XPATH, '//android.widget.EditText')
    FRENCH_OPTION = (By.XPATH, '//android.widget.TextView[@text="Français"]')

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.timeout = timeout

    def change_language(self, language):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(self.LANGUAGE_BTN)
            ).click()
            print("Bouton 'Language' cliqué")
        except TimeoutException:
            print("Bouton 'Language' non trouvé")

        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(self.LOOP_BTN)
            ).click()
            print("Bouton cible de la liste cliqué")
        except TimeoutException:
            print("Bouton cible non trouvé")

        try:
            input_field = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(self.INPUT_FIELD)
            )
            input_field.send_keys(language)
            french_option = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(self.FRENCH_OPTION)
            )
            french_option.click()
            
            print(f"Texte '{language}' saisi dans le champ")
        except TimeoutException:
            print("Champ input introuvable")
