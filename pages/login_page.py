from selenium.webdriver.common.by import By
from utils.events import BasePage

class LoginPage(BasePage):


    CONTACT_BTN = (By.XPATH, "//nav[@class='navbar navbar-expand-lg navbar-light']/div/div/ul[2]/li[2]")
    FULL_NAME= (By.XPATH,"//div[@class='contact-sales']//div[@id='Form_getForm_FullName_Holder']")


    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def fill_contact_form(self,fullname):
        self.click(self.CONTACT_BTN)
        self.enter_text(self.FULL_NAME, fullname)
