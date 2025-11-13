from appium import webdriver
from appium.options.common.base import AppiumOptions

class DriverFactory:

    driver = None

    @staticmethod
    def start_driver():
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:deviceName": "emulator-5556",
            "appium:app": "/Users/vincenthouri/Downloads/app-alpha-universal-release.apk",
            "appium:appPackage": "org.wikipedia.alpha",
            "appium:appActivity": "org.wikipedia.main.MainActivity",
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True,
            "appium:chromedriverAutodownload": True
        })

        DriverFactory.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

        print("L'application est lancée sur l'émulateur !")

        # Garder le script ouvert pour tester
        return DriverFactory.driver

    def quit_driver():
        if DriverFactory.driver:
            DriverFactory.driver.quit()
            DriverFactory.driver = None

