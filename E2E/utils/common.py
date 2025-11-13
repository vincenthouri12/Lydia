
def click_button(driver, by, value):
    button = driver.find_element(by, value)
    button.click()

def enter_text(driver, by, value, text):
    input_field = driver.find_element(by, value)
    input_field.clear()
    input_field.send_keys(text)

def check_element_exists(driver, by, value):
    elements = driver.find_elements(by, value)
    
    return len(elements) > 0