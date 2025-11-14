from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchPage:
    SEARCH_INPUT = (By.XPATH, '//android.widget.TextView[@text="Search Wikipedia"]')
    SEARCH_FOCUSED = (By.ID, 'org.wikipedia.alpha:id/search_src_text')
    FIRST_RESULT = (By.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="org.wikipedia.alpha:id/search_results_list"]/android.view.ViewGroup[1]')
    TARGET_LYDIA = (By.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/page_list_item_description" and @text="Ancient Anatolian kingdom"]')

    def __init__(self, driver):
        self.driver = driver

    def search_city(self, term):
        try:
            input_search = self.driver.find_element(*self.SEARCH_INPUT)
            input_search.click()
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.SEARCH_FOCUSED))
            input_search_focused = self.driver.find_element(*self.SEARCH_FOCUSED)
            input_search_focused.send_keys(term)
            print(f"Terme '{term}' saisi dans la recherche")
            time.sleep(1) 
        except NoSuchElementException:
            print("Input de recherche introuvable !")

    def click_city(self, term):
        try:
            item = self.driver.find_element(*self.TARGET_LYDIA)
            item.click()
            print(f"Résultat '{term}' cliqué")
            return
        except NoSuchElementException:
            print("Liste de résultats introuvable !")
