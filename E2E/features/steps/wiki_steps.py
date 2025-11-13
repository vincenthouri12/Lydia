from behave import given, when, then
from utils.driver import DriverFactory
from pages.carousel import CarouselPage
from pages.search_page import SearchPage
from pages.popup import PopupPage
from pages.language import LanguagePage
from pages.cresus import CresusPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given("the user launchs the app")
def step_launch_app(context):
    pass
    # context.driver = DriverFactory.start_driver()

@when('the user is on the carrousel')
def step_on_carrousel(context):
    start_carrousel = context.driver.find_elements(By.XPATH, '//android.widget.LinearLayout[@resource-id="org.wikipedia.alpha:id/scrollViewContainer"]')
    assert start_carrousel

@when('the user handles the carrousel')
def do_carrousel(context):
    CarouselPage(context.driver).handle_carousel()

@then('the user is on the app')
def step_verify(context):
    # WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.ID, 'org.wikipedia.alpha:id/navigation_bar_item_content_container')))
    feed = context.driver.find_elements(By.XPATH, '//androidx.recyclerview.widget.StaggeredGridLayoutManager[@resource-id="org.wikipedia.alpha:id/feed_view"]')
    assert feed
    # DriverFactory.quit_driver()

@given('the user is on the homepage of the app')
def step_user_on_app(context):
    pass

@when('the user searches for Lydia city')
def step_search_city(context):
    time.sleep(1)
    search = SearchPage(context.driver)
    search.search_city("Lydia")
    search.click_city("Lydia")
    PopupPage(context.driver).close_popup_if_present()

@then('the Lydia page is displayed')
def step_verify_city_page(context): 
    lydia_title = context.driver.find_elements(By.XPATH, '(//android.widget.TextView[@text="Lydia"])[1]')
    assert lydia_title
    
@given('the user is on the lydia city page')
def step_user_on_lydia_page(context):
    pass

@when('the user changes the app language to french')
def step_change_language(context):
    LanguagePage(context.driver).change_language("français")

@then('the lydia page is displayed in french')
def step_verify_lydia_in_french(context):
    lydia_title_fr = context.driver.find_elements(By.XPATH, '(//android.widget.TextView[@text="Lydie"])[1]')
    assert lydia_title_fr

@given('the user is on the lydia city page in french')
def step_user_on_lydia_page_fr(context):
    pass

@when('the user scrolls to the Cresus section')
def step_scroll_to_cresus(context):
    CresusPage(context.driver).scroll_to_crésus_and_click()

@when('the user clicks on the Cresus section')
def step_click_cresus_section(context):
    CresusPage(context.driver).click_preview_if_visible()

@then('the Cresus page is displayed')
def step_verify_cresus_page(context):
    CresusPage(context.driver).verify_crésus_displayed()