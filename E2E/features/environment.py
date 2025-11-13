from appium import webdriver
from appium.options.common.base import AppiumOptions

def before_all(context):
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

    context.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    context.driver.implicitly_wait(10)
    print("🚀 Appium driver initialisé")


def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()
        print("🧹 Session Appium terminée proprement")