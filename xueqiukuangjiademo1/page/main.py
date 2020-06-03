from selenium.webdriver.common.by import By

from xueqiukuangjiademo1.page.basepage import BasePage
from xueqiukuangjiademo1.page.market import Market


class Main(BasePage):
    def goto_market(self):
        # click
        self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        return Market(self._driver)