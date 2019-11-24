from selenium import webdriver


class WebDriver:

    __instance = False

    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=option)

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        cls.__instance = object.__new__(WebDriver, *args, **kwargs)
        return cls.__instance