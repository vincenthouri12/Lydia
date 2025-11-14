from utils.driver import DriverFactory
from pages.carousel import CarouselPage
from pages.search_page import SearchPage
from pages.popup import PopupPage
from pages.language import LanguagePage
from pages.cresus import CresusPage


if __name__ == '__main__':
    driver = DriverFactory.start_driver()
    CarouselPage(driver).handle_carousel()
    SearchPage(driver).search_city("Lydia")
    SearchPage(driver).click_city("Lydia") 
    PopupPage(driver).close_popup_if_present()
    LanguagePage(driver).change_language("français")
    CresusPage(driver).scroll_to_crésus_and_click()
    CresusPage(driver).click_preview_if_visible()
    CresusPage(driver).verify_crésus_displayed()


    input("Appuyez sur Entrée pour fermer l'application et quitter...")
    DriverFactory.quit_driver()