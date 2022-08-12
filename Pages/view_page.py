from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class view_homepage:
    def __int__(self, driver):
        self.driver = driver
        self.drop_down_selector = "//div[@class='mat-select-panel-wrap ng-tns-c60-1 ng-trigger ng-trigger-transformPanelWrap ng-star-inserted']"
        self.search_field = "//app-root/div[@class='container-fluid']/app-asset-or-project[@class='ng-star-inserted']/div//app-search//input[@type='text']"
        self.search_button = "//mat-icon[normalize-space()='search']"
        self.create_risk_profile_button = "//button[@class='blue-button']"
        self.expand_more = "//div[normalize-space()='Richmond Refinery - Utilities & Environmental']"
        self.expand_more_50 = "//span[normalize-space()='50']"
        self.expand_more_100 = "//span[normalize-space()='100']"
    def pagination_click_50(self):
        self.find_element(By.XPATH, self.drop_down_selector ).click()
        self.find_element(By.XPATH, self.expand_more_50).click()

    def pagination_click_100(self):
        self.find_element(By.XPATH, self.drop_down_selector).click()
        self.find_element(By.XPATH, self.expand_more_100).click()


