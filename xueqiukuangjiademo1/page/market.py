from xueqiukuangjiademo1.page.basepage import BasePage
from xueqiukuangjiademo1.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self._driver)
